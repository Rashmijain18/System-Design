import argparse
import redis
import requests
import json
import sys

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
CACHE_TTL = 600  # 10 minutes

WEATHER_API_URL = 'https://api.weather.gov'

def get_redis_client():
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

def get_weather_from_api(city):
    # Step 1: Get lat/lon from city name using Nominatim (OpenStreetMap)
    geocode_url = f"https://nominatim.openstreetmap.org/search"
    geocode_params = {
        'q': city,
        'format': 'json',
        'limit': 1
    }
    geo_resp = requests.get(geocode_url, params=geocode_params, headers={"User-Agent": "weather-cli-app"})
    if geo_resp.status_code != 200 or not geo_resp.json():
        print(f"Error geocoding city: {geo_resp.status_code}", file=sys.stderr)
        return None
    geo = geo_resp.json()[0]
    lat, lon = geo['lat'], geo['lon']

    # Step 2: Get weather.gov gridpoint for lat/lon
    points_url = f"{WEATHER_API_URL}/points/{lat},{lon}"
    points_resp = requests.get(points_url, headers={"User-Agent": "weather-cli-app"})
    if points_resp.status_code != 200:
        print(f"Error getting gridpoint: {points_resp.status_code}", file=sys.stderr)
        return None
    points_data = points_resp.json()
    forecast_url = points_data['properties']['forecast']

    # Step 3: Get forecast
    forecast_resp = requests.get(forecast_url, headers={"User-Agent": "weather-cli-app"})
    if forecast_resp.status_code == 200:
        return forecast_resp.json()
    else:
        print(f"Error fetching weather: {forecast_resp.status_code}", file=sys.stderr)
        return None

def main():
    parser = argparse.ArgumentParser(description='Get weather for a city (with Redis cache)')
    parser.add_argument('city', type=str, help='City name')
    args = parser.parse_args()
    city = args.city.strip().lower()
    cache_key = f"weather:{city}"

    r = get_redis_client()
    cached = r.get(cache_key)
    if cached:
        print("[Cache]", cached.decode('utf-8'))
        return

    weather = get_weather_from_api(city)
    if weather:
        weather_json = json.dumps(weather)
        r.setex(cache_key, CACHE_TTL, weather_json)
        print("[API]", weather_json)
    else:
        print("Could not get weather data.", file=sys.stderr)

if __name__ == '__main__':
    main()
