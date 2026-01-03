# Redis in System Design

This document contains notes and explanations about Redis, its use cases, and how it fits into system design.

## What is Redis?

Redis is an open-source, in-memory data structure store, used as a database, cache, and message broker. It is known for its speed and versatility. It follows a key–value model where each key maps to exactly one data type, and commands operate on keys and their values

“In-memory” means data is kept directly in the computer’s main memory (RAM) instead of on slower storage like disks or SSDs. This makes reading and writing that data much faster,

can i use redis in frontend? with react? or only designed for backend?
Redis is designed to run on the server (backend - (Node, Python, Go, Java, etc.)), not directly in the browser, so you do not connect to Redis from React the way you connect to, for example, localStorage or browser APIs.

## Common Use Cases

- Caching
  Caching means keeping a copy of frequently used data in Redis so you don’t have to recompute it or hit a slower database every time.

  A common pattern is “cache-aside”: your code first looks in Redis; if the data is there (cache hit), it returns it, otherwise it reads from the database, stores it in Redis, then returns it (cache miss).

  You usually set a TTL (expiry) for keys so stale data eventually gets evicted, and you might also evict/update cache entries when the underlying data changes.

- Session management
  Session management means storing per-user state (logged-in user info, preferences, etc.) so it can be quickly retrieved on each request.

  Many web frameworks can plug their session store into Redis; they store a session ID in a cookie and the real session data (user id, roles, small bits of state) under a key like session:<id> in Redis.

  Redis fits this well because sessions are small, frequently read on every request, and often expire after some inactivity period, which maps directly to key TTLs.

- Real-time analytics
  Real-time analytics means tracking counters and metrics that are updated and read very frequently with low latency.

  Redis can maintain rolling counters, dashboards, and leaderboards using structures like strings (for counters), hashes (for grouped metrics), and sorted sets (for top-N lists).

  Typical examples: page view counters, active users, live scores, or ranking lists that update in real time as users interact with your app.

- Pub/Sub messaging
  Pub/Sub (publish/subscribe) is a messaging pattern where senders publish messages to channels and receivers subscribe to those channels.

  With Redis pub/sub, a producer publishes to a channel like chat:room:1, and any clients subscribed to that channel receive the message instantly.

  This is useful for things like chat, notifications, and broadcasting events to multiple services or WebSocket servers, though for durable messaging and replay you’d typically use Redis Streams instead of simple pub/sub.

## Why Use Redis in System Design?

Redis helps improve system performance, scalability, and reliability by providing fast data access and supporting distributed architectures.

## Redis Data Structures

- **Strings**: Basic key-value pairs.
- **Lists**: Ordered collections, useful for queues.
- **Sets**: Unordered, unique values.
- **Sorted Sets**: Sets ordered by score, great for leaderboards.
- **Hashes**: Field-value pairs, like a dictionary.
- **Streams, Bitmaps, HyperLogLogs**: Advanced use cases.

Redis is a key–value store where every entry is a key mapped to exactly one value, but that “value” can be a rich data structure like a list, set, hash, or stream, not just a simple string. So it is both a key–value database and a data-structure server.
​
Big picture: key → data structure
Every piece of data in Redis is stored under a key, for example user:1, queue:emails, or leaderboard:game1.​

For each key, you choose one type (string, list, set, hash, sorted set, etc.), and all commands on that key must match its type; you cannot treat the same key as both a list and a hash.

So you always have a key, but what the key points to is often more complex than a plain scalar value.

## Best Practices for Redis Caching

It is important to consider a few best practices when working with Redis caching:

- Identify the Right Data to Cache: Not all data needs to be cached. Focus on caching data that is frequently accessed or computationally expensive to generate. This includes data that doesn't change frequently or can be shared across multiple requests.
- Set Expiration Policies: Determine an appropriate expiration policy for cached data. This ensures that the cache remains up to date and avoids serving stale data. Set expiration times based on the frequency of data updates and the desired freshness of the cached data.
- Implement Cache Invalidation: When the underlying data changes, it is essential to invalidate or update the corresponding cache entries. This can be done by using techniques such as cache invalidation triggers or monitoring changes in the data source.
- Monitor Cache Performance: Regularly monitor the performance of the cache to ensure its effectiveness. Keep an eye on cache hit rates, cache misses, and overall cache utilization. Monitoring can help identify potential bottlenecks or areas for optimization.
- Scale Redis for High Traffic: As your application's traffic grows, consider scaling Redis to handle the increased load. This can involve using Redis clusters or replication to distribute the data across multiple instances and increase read and write throughput.

## Scalability

- **Replication**: Master-slave for high availability.
- **Sharding**: Partition data across instances.
- **Cluster Mode**: Automatic sharding and failover.

## Security

- Use strong passwords (`AUTH` command).
- Enable TLS for encrypted connections.
- Restrict access with firewalls.

---

## How to Connect and Setup Redis in Python

1. **Install Redis Server**

   - macOS: `brew install redis`
   - Linux: `sudo apt-get install redis-server`
   - Windows: Use Docker or WSL.

2. **Start Redis Server**

   - Run: `redis-server` (default port 6379)

3. **Install Python Client**

   - `pip install redis`

4. **Connect in Python**

   ```python
   import redis
   r = redis.Redis(host='localhost', port=6379, db=0)
   r.set('foo', 'bar')
   print(r.get('foo'))  # Output: b'bar'
   ```

5. **Common Operations**

   - Set: `r.set('key', 'value')`
   - Get: `r.get('key')`
   - Delete: `r.delete('key')`
   - List: `r.lpush('mylist', 'item')`, `r.lrange('mylist', 0, -1)`
   - Hash: `r.hset('myhash', 'field', 'value')`, `r.hget('myhash', 'field')`

6. **Connection Pooling**
   ```python
   pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
   r = redis.Redis(connection_pool=pool)
   ```

## How to check if Redis is running in Docker:

Run this command in your terminal to connect to Redis CLI inside the Docker container:
docker exec -it redis-server redis-cli

Once inside the Redis CLI, you can type commands like:
ping
It should reply with PONG.

To see keys stored in Redis:
keys \*
