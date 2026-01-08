## Topics You’ll Learn (Python + Infra)

### Python

- Basic Python syntax
- HTTP server
- Environment variables
- API endpoints

### NGINX

- Reverse proxy
- Load balancing
- Health checks
- Failure handling

---

## Architecture

```
Browser
   ↓
NGINX (Load Balancer)
   ↓
FastAPI App 1
FastAPI App 2
FastAPI App 3
```

---

## Project Structure

```
nginx-python-lb/
├── docker-compose.yml
├── nginx/
│   └── nginx.conf
└── app/
    ├── Dockerfile
    ├── main.py
    └── requirements.txt
```

---

## STEP 1: Python Backend (FastAPI)

### `app/main.py`

```python
from fastapi import FastAPI
import os

app = FastAPI()

SERVER_NAME = os.getenv("SERVER_NAME", "UNKNOWN")

@app.get("/")
def read_root():
    return {"message": f"Response from {SERVER_NAME}"}

@app.get("/health")
def health():
    return {"status": "ok"}
```

---

### `app/requirements.txt`

```
fastapi
uvicorn
```

---

### `app/Dockerfile`

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## STEP 2: NGINX Load Balancer Config

### `nginx/nginx.conf`

```nginx
events {}

http {
    upstream python_backends {
        server app1:8000;
        server app2:8000;
        server app3:8000;
    }

    server {
        listen 80;

        location / {
            proxy_pass http://python_backends;
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
}
```

---

## STEP 3: Docker Compose

### `docker-compose.yml`

```yaml
version: "3.8"

services:
  nginx:
    image: nginx:latest
    ports:
      - "8080:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - app1
      - app2
      - app3

  app1:
    build: ./app
    environment:
      - SERVER_NAME=PY_APP_1

  app2:
    build: ./app
    environment:
      - SERVER_NAME=PY_APP_2

  app3:
    build: ./app
    environment:
      - SERVER_NAME=PY_APP_3
```

---

## STEP 4: Run the Project 🚀

```bash
docker compose up --build
```

Open browser:

```
http://localhost:8080
```

Refresh → you should see responses rotating between:

- PY_APP_1
- PY_APP_2
- PY_APP_3

---

## What You Just Learned

✔ NGINX works with Python
✔ Load balancing is language-agnostic
✔ Python + FastAPI basics
✔ Real production-style infra

You’re learning **Python + system design together** — very smart.

---

## What We Can Do Next (Highly Recommended)

Next upgrades (in order):

1️⃣ **NGINX health checks** using `/health`
2️⃣ Simulate backend failure
3️⃣ Sticky sessions
4️⃣ SSL termination
5️⃣ Rate limiting
6️⃣ Python logging + request tracing

---

## Interview-Ready One-Liner

> “I built an NGINX layer-7 load balancer in front of multiple FastAPI services using Docker Compose, implementing traffic distribution and health checks.”

---

### 👉 Next Step

Run this setup **now**.
Reply with:

- “Working” ✅
- or paste any error ❌

We’ll level it up step-by-step 🔥
