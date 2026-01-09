# 📘 System Design – Complete Study Plan

## Phase 0: Foundations & Design Thinking

> Goal: Learn how to think like a system designer

- [x] **High-level principles**
      _Concepts:_ scalability, availability, reliability, fault tolerance, latency vs throughput
      _Exercise:_ Explain trade-offs for a **read-heavy vs write-heavy** system.

- [x] **Requirement gathering & design process**
      _Concepts:_ functional vs non-functional, constraints, SLA / SLI / SLO
      _Exercise:_ Write requirements for a **URL shortener**.

- [x] **Design documentation & communication**
      _Concepts:_ design docs, diagrams, ADRs, reviews
      _Exercise:_ Write a **1-page design doc** for a notification system.

- [x] **User experience in distributed systems**
      _Concepts:_ latency perception, errors, graceful degradation
      _Exercise:_ Design UX behavior when a dependency is slow or down.

---

## Phase 1: Networking & Traffic Management

> Goal: Understand request flow end-to-end

- [ ] **Networking fundamentals**
      _Concepts:_ TCP/IP, DNS, HTTP/HTTPS, TLS, TCP vs UDP, NAT, proxies
      _Exercise:_ Trace an HTTP request and identify latency sources.

- [x] **Load balancing & proxies**
      _Concepts:_ L4 vs L7, sticky sessions, health checks,
      _Exercise:_ Design a global load-balancing strategy.

- [ ] **Azure service bus, Azure function,scheduler,task schedular**
      _Concepts:_ Azure service bus
      _Exercise:_ Implement azure service bus

-[ ] **Reverse proxy, forward proxy**

- [ ] **API gateway & service mesh**
      _Concepts:_ centralized auth, retries, traffic shaping
      _Exercise:_ Design API gateway rules for 10 microservices.

- [ ] **Rate limiting & throttling**
      _Concepts:_ token bucket, leaky bucket, distributed counters
      _Exercise:_ Design rate limiting with burst tolerance.

---

## Phase 2: Data Storage & Modeling

> Goal: Choose and model data correctly

- [ ] **Databases: fundamentals**
      _Concepts:_ SQL vs NoSQL, ACID, BASE, indexes
      _Exercise:_ Choose DBs for an **e-commerce order system**.

- [ ] **Data modeling & schema design**
      _Concepts:_ access patterns, denormalization
      _Exercise:_ Model schema for **time-series metrics**.

- [ ] **Indexing & search**
      _Concepts:_ inverted index, ranking, sharding
      _Exercise:_ Design search for an article platform.

- [ ] **Storage systems & object stores**
      _Concepts:_ S3, multipart upload, consistency
      _Exercise:_ Design large file upload/download service.

- [ ] **Metadata, tagging & searchability**
      _Concepts:_ faceted search, query planning
      _Exercise:_ Design tag-based search for a photo app.

---

## Phase 3: Scalability, Performance & Caching

> Goal: Handle scale efficiently

- [ ] **Caching**
      _Concepts:_ CDN, Redis, eviction, invalidation
      _Exercise:_ Design caching for user profiles.

- [ ] **Capacity planning & scaling**
      _Concepts:_ RPS math, bottlenecks
      _Exercise:_ Estimate servers needed for X RPS.

- [ ] **Performance engineering**
      _Concepts:_ profiling, benchmarking, load testing
      _Exercise:_ Identify bottlenecks from load-test results.

- [ ] **CDN & edge computing**
      _Concepts:_ signed URLs, edge logic
      _Exercise:_ Design media delivery with CDN.

---

## Phase 4: Distributed Systems & Consistency

> Goal: Build correct distributed systems

- [ ] **Replication & consistency**
      _Concepts:_ leader-follower, multi-leader, Raft basics
      _Exercise:_ Design replicated DB with failover.

- [ ] **Partitioning / sharding**
      _Concepts:_ sharding keys, rebalancing
      _Exercise:_ Shard a user table and handle growth.

- [ ] **Consistency patterns**
      _Concepts:_ eventual, session, causal
      _Exercise:_ Handle stale reads in an eventually consistent system.

- [ ] **Concurrency & distributed systems basics**
      _Concepts:_ locks, leader election
      _Exercise:_ Design distributed lock using Redis/ZooKeeper.

- [ ] **Advanced distributed algorithms (optional)**
      _Concepts:_ CRDTs, vector clocks
      _Exercise:_ Build simple CRDT for collaborative edits.

---

## Phase 5: Async & Event-Driven Architectures

> Goal: Decouple systems

- [ ] **Message queues & streaming**
      _Concepts:_ Kafka, pub/sub, ordering
      _Exercise:_ Design analytics ingestion pipeline.

- [ ] **Async processing & background jobs**
      _Concepts:_ retries, idempotency, DLQs
      _Exercise:_ Design retry + backoff strategy.

- [ ] **Event-driven architectures**
      _Concepts:_ Sagas, CQRS, event sourcing
      _Exercise:_ Design payment workflow using Saga.

- [ ] **Data migration strategies**
      _Concepts:_ live migration, schema evolution
      _Exercise:_ Plan zero-downtime DB migration.

---

## Phase 6: Microservices & Platform Architecture

> Goal: Scale teams and systems

- [ ] **Microservices & SOA**
      _Concepts:_ service boundaries, contracts
      _Exercise:_ Break monolith into microservices.

- [ ] **Multi-region architectures**
      _Concepts:_ geo-replication, latency
      _Exercise:_ Design active-active global system.

- [ ] **Legacy system integration**
      _Concepts:_ strangler pattern
      _Exercise:_ Migrate legacy auth system safely.

- [ ] **Mobile/backend integration**
      _Concepts:_ offline sync, push notifications
      _Exercise:_ Design offline-first mobile sync.

---

## Phase 7: Reliability, Security & Operations

> Goal: Run systems safely

- [ ] **Fault tolerance & resiliency patterns**
      _Concepts:_ circuit breakers, bulkheads
      _Exercise:_ Protect system from flaky dependency.

- [ ] **Disaster recovery planning**
      _Concepts:_ RTO/RPO, DR drills
      _Exercise:_ Design DR for payment system.

- [ ] **Observability & monitoring**
      _Concepts:_ metrics, logs, tracing
      _Exercise:_ Define SLIs and alerts.

- [ ] **Security basics**
      _Concepts:_ OAuth, JWT, encryption
      _Exercise:_ Design auth flow for third-party API.

- [ ] **Data durability & backups**
      _Concepts:_ PITR, snapshots
      _Exercise:_ Test restore from backup.

---

## Phase 8: DevOps, Cloud & Cost

> Goal: Ship efficiently

- [ ] **Deployment & CI/CD**
      _Concepts:_ Docker, Kubernetes, canary
      _Exercise:_ Design zero-downtime deploy.

- [ ] **Infrastructure as Code (IaC)**
      _Concepts:_ Terraform, reproducibility
      _Exercise:_ Model infra as code.

- [ ] **Cloud-native patterns**
      _Concepts:_ managed services trade-offs
      _Exercise:_ Replace self-managed DB with managed DB.

- [ ] **Cost optimization & multi-cloud**
      _Concepts:_ autoscaling, cost models
      _Exercise:_ Estimate monthly cloud cost.

- [ ] **Vendor lock-in & exit strategies**
      _Concepts:_ portability
      _Exercise:_ Design cloud-agnostic storage.

---

## Phase 9: Specialized Systems

- [ ] **Graph systems & social graphs**
      _Exercise:_ Design follower/followee system.

- [ ] **Time-series databases & analytics**
      _Exercise:_ Design metrics storage with rollups.

---

## Phase 10: Ethics, Compliance & Sustainability

- [ ] **Legal, privacy & compliance**
      _Exercise:_ Identify GDPR risks.

- [ ] **Ethics in system design**
      _Exercise:_ Analyze bias risk in recommendation system.

- [ ] **Green computing & sustainability**
      _Exercise:_ Reduce energy footprint of architecture.

---

## Phase 11: Real-World Mastery

- [ ] **Real-world case studies**
      _Exercise:_ Analyze a major outage postmortem.

- [ ] **Team collaboration & reviews**
      _Exercise:_ Conduct mock design review.

- [ ] **Emerging topics**
      _Exercise:_ Evaluate serverless vs containers.

---
