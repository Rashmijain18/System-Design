## How to use this list

Start at the top and move down. Tackle core items first, then return to advanced topics and operational concerns. Time estimates assume part-time study (5–10 hours/week).

## Full topic list (ordered, with notes & exercises)

1. High-level principles (priority: high, 1 week)

   - Concepts: scalability, availability, fault tolerance, reliability, latency vs throughput, trade-offs.
   - Exercise: explain trade-offs for a read-heavy vs write-heavy app.

2. Requirement gathering and design process (high, 1–2 days)

   - Techniques: clarify, scope, constraints, SLA/SLI/SLO.
   - Exercise: write functional and non-functional requirements for a URL shortener.

3. Networking fundamentals (high, 1 week)

   - Topics: TCP/IP, DNS, HTTP/HTTPS, TLS, TCP vs UDP, ports, proxies, NAT.
   - Exercise: trace an HTTP request end-to-end and identify latency sources.

4. Load balancing and proxies (high, 3 days)

   - Topics: L4 vs L7, sticky sessions, reverse proxy, HAProxy, Nginx, health checks.
   - Exercise: design LB strategy for global services.

5. Caching (high, 1 week)

   - Topics: CDN, browser cache, edge caching, origin cache, in-memory caches (Redis/Memcached), eviction policies, cache invalidation.
   - Exercise: design a caching layer for user profiles and explain invalidation.

6. Databases: fundamentals (high, 2 weeks)

   - Topics: SQL vs NoSQL, normalization, indexes, transactions, ACID, BASE.
   - Exercise: choose DB for an e-commerce order system and justify.

7. Replication and consistency (high, 1 week)

   - Topics: master-slave, multi-master, consensus (Paxos, Raft basics), eventual vs strong consistency.
   - Exercise: design a replicated leader-follower DB with failover.

8. Partitioning / Sharding (high, 1 week)

   - Topics: horizontal vs vertical scaling, sharding keys, re-sharding, consistent hashing.
   - Exercise: shard a user table and handle rebalancing.

9. Data modeling & schema design (high, 3–4 days)

   - Topics: choosing the right model for access patterns, denormalization, wide-column stores.
   - Exercise: model schema for time-series metrics.

10. Indexing and search (medium, 1 week)

    - Topics: inverted index, full-text search, Elasticsearch, sharding/search ranking.
    - Exercise: design search for an article site.

11. Message queues and streaming (high, 1 week)

    - Topics: queue vs pub/sub, Kafka, RabbitMQ, SQS, ordering, retention, partitioning.
    - Exercise: design an event pipeline for analytics ingestion.

12. Asynchronous processing & background jobs (medium, 3–4 days)

    - Topics: workers, retries, idempotency, dead-letter queues.
    - Exercise: build a retry/backoff strategy for failed jobs.

13. Microservices & service-oriented architecture (medium, 1 week)

    - Topics: service boundaries, API contracts, service discovery, versioning, fallbacks.
    - Exercise: split a monolith into microservices and design inter-service communication.

14. APIs & API design (high, 3–4 days)

    - Topics: REST vs gRPC, design principles, pagination, rate limiting, versioning.
    - Exercise: design a REST API for posts with pagination and rate limits.

15. Consistency patterns (medium, 3 days)

    - Topics: read-after-write, session consistency, causal consistency, monotonic reads.
    - Exercise: implement eventual consistency example and handle stale reads.

16. Concurrency & distributed systems basics (high, 1 week)

    - Topics: race conditions, distributed locks, leader election, consensus.
    - Exercise: design a distributed lock using Redis or ZooKeeper.

17. Rate limiting & throttling (medium, 2–3 days)

    - Topics: token bucket, leaky bucket, distributed counters.
    - Exercise: implement rate limiter design for API with burst tolerance.

18. Security basics (high, ongoing)

    - Topics: authentication (OAuth, JWT), authorization, encryption at rest/in transit, secrets management.
    - Exercise: design auth flow for third-party API.

19. Data durability & backups (medium, 2–3 days)

    - Topics: backups, snapshots, point-in-time recovery, archival.
    - Exercise: plan backup and restore for a transactional DB.

20. Observability & monitoring (high, 1 week)

    - Topics: metrics, logs, tracing (OpenTelemetry, Jaeger), SLIs/SLOs/SLAs, alerting.
    - Exercise: define SLIs and alerts for an API service.

21. Deployment & CI/CD (medium, 1 week)

    - Topics: pipelines, containerization, Docker, Kubernetes basics, blue/green, canary deployments.
    - Exercise: design deploy strategy for zero-downtime releases.

22. Capacity planning & scaling (high, 3–4 days)

    - Topics: load estimation, throughput calculations, bottleneck identification.
    - Exercise: estimate servers needed for X RPS and Y payload.

23. Fault tolerance & resiliency patterns (high, 1 week)

    - Topics: circuit breaker, bulkhead, retries with backoff, graceful degradation.
    - Exercise: apply circuit breaker to a flaky external API call.

24. CDN & edge computing (medium, 3 days)

    - Topics: CDN caching, signed URLs, edge functions.
    - Exercise: design media-serving pipeline with CDN and signed access.

25. Storage systems & object stores (medium, 3–4 days)

    - Topics: S3-like storage, multipart upload, eventual consistency in object stores.
    - Exercise: design large-file upload and retrieval service.

26. Graph systems & social graphs (medium, 1 week)

    - Topics: graph databases, adjacency lists, traversals, friend recommendations.
    - Exercise: design follower/followee storage for a social app.

27. Time-series databases and analytics (medium, 4 days)

    - Topics: TSDBs, rollups, retention policies, OLAP vs OLTP.
    - Exercise: design metrics store for monitoring.

28. Metadata, tagging, & searchability (low-medium, 3 days)

    - Topics: indexing metadata, faceted search, query planning.
    - Exercise: design tag-based search for photo app.

29. Event-driven architectures & eventual consistency (medium, 1 week)

    - Topics: compensation transactions, sagas, event sourcing, CQRS.
    - Exercise: design payment workflow using saga pattern.

30. Advanced distributed algorithms (low, optional)

    - Topics: Paxos/Raft deep dive, vector clocks, CRDTs.
    - Exercise: build simple CRDT example for collaborative edits.

31. Cost optimization & multi-cloud (medium, ongoing)

    - Topics: spot instances, autoscaling policies, data transfer costs.
    - Exercise: estimate monthly cost for your design and propose reductions.

32. Legal, privacy, compliance (low-medium, ongoing)

    - Topics: GDPR, data residency, audit logging, retention policies.
    - Exercise: identify compliance risks for user data storage.

33. Emerging topics (as needed)

    - Topics: edge computing, serverless patterns, WebAssembly at edge, ML infra considerations.
    - Exercise: evaluate serverless vs containers for a use case.

## Study tips and exercises

- Always start designs by clarifying requirements and numbers.
- Work backward from access patterns to choose storage and indexing.
- Build small prototypes (URL shortener, file store, timeline) to cement concepts.
- Time-box mock interviews and get feedback focusing on trade-offs and clarity.
