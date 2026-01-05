## 1. Scalability

Scalability is how well a system can handle **increasing load** (more users, data, or requests) by **adding resources**, rather than rewriting large parts of the system.

A scalable system grows **predictably and economically** as demand increases.

---

### Types of Scaling

#### Vertical Scaling (Scale Up)

- Add more power to a single machine (CPU, RAM, disk, network).
- Simple to implement.
- Limited by hardware and creates a single point of failure.

**Example**
Upgrading a database server from 8 GB RAM to 64 GB RAM to handle more queries.

---

#### Horizontal Scaling (Scale Out)

- Add more machines and distribute traffic or data across them.
- Achieved using load balancers, clustering, and sharding.
- Enables very large-scale systems.

**Example**
Adding multiple API servers behind a load balancer so each server handles only a fraction of incoming requests.

---

### Design Principles for Scalability

- Stateless application servers.
- Caching layers (Redis, CDN).
- Database sharding and partitioning.
- Asynchronous processing using queues.
- Elastic infrastructure (auto-scaling).

### **1. Stateless Application Servers**

- **What it means:** Each server that runs your application doesn’t remember any user-specific data between requests. All the data needed to process a request comes from the request itself or an external system (like a database or cache).
- **Why it matters:** Makes it easy to add or remove servers because any server can handle any request.
- **Example:** A web app where users log in. Instead of storing session info on the server, the app stores it in a shared database or in a token (like JWT). Then, if one server goes down, another server can continue without losing user sessions.

---

### **2. Caching Layers (Redis, CDN)**

- **What it means:** Store frequently accessed data temporarily so your servers don’t have to recompute or fetch it from the main database every time.
- **Why it matters:** Reduces database load and improves response times.
- **Examples:**

  - **Redis:** An in-memory key-value store, great for caching database query results.
  - **CDN (Content Delivery Network):** Stores static assets (images, CSS, JS) closer to users, reducing latency.

---

### **3. Database Sharding and Partitioning**

- **What it means:** Split your database into smaller parts (shards) so no single database has to handle all the data.
- **Why it matters:** Helps databases handle more users and data without slowing down.
- **Example:** A social media app splits users by region:

  - Users from the US go to DB1, users from Europe go to DB2, etc.
  - Each shard is smaller, faster, and easier to scale.

---

### **4. Asynchronous Processing Using Queues**

- **What it means:** Some tasks don’t need to happen immediately, so instead of making the user wait, you put them in a **queue** to be processed later.
- **Why it matters:** Prevents your servers from getting overloaded and improves user experience.
- **Example:** Sending emails after a user signs up. Instead of sending the email immediately while the user waits, you put the email task in a queue (like RabbitMQ or AWS SQS) and a worker processes it in the background.

---

### **5. Elastic Infrastructure (Auto-Scaling)**

- **What it means:** Automatically add or remove servers based on the current load.
- **Why it matters:** Saves costs when traffic is low and ensures your app can handle traffic spikes.
- **Example:** An online store during Black Friday:

  - Traffic spikes to 10x normal. Auto-scaling adds more servers automatically.
  - After the sale, extra servers are removed to save money.

---

### Practical Scenario

An API handles 1,000 requests/min on one server.
During a sale, traffic jumps to 50,000 requests/min:

- Vertical scaling reaches CPU limits.
- Horizontal scaling adds more app servers and spreads load.
- Cache reduces database pressure, allowing smoother scaling.

---

### Key Idea

**Scalability answers:** _Can the system grow without breaking?_

---

## 2. Availability

Availability is the **percentage of time** a system is operational and able to serve requests.

It focuses only on whether the system responds, not whether responses are correct or fast.

---

### Availability Levels

- 99% → ~3.65 days downtime/year
- 99.9% → ~8.76 hours/year
- 99.99% → ~52 minutes/year

---

### Practical Example

- A single database server crashes → entire site goes down.
- Adding a replica in another zone with automatic failover:

  - Primary fails
  - Replica takes over
  - Users see minimal disruption

---

### Techniques to Improve Availability

- Redundant service instances.
- Health checks and automatic restarts.
- Multi-zone or multi-region deployments.
- Load balancers with failover logic.

---

### Key Idea

**Availability answers:** _Is the system reachable right now?_

---

## 3. Reliability

Reliability is how **consistently and correctly** a system behaves over time, including under failures and heavy load.

A reliable system:

- Returns correct results.
- Does not lose or corrupt data.
- Behaves predictably.

---

### Practical Example

An order service accepts payment but sometimes fails to create the order record:

- The system is available (it responds).
- The system is unreliable (incorrect behavior).

---

### Reliability Techniques

- Redundancy (multiple service instances).
- Data replication.
- Idempotent APIs (safe retries).
- Transactions for atomic operations.
- Durable storage.
- Monitoring, alerting, and backups.
- Automatic failover.

Idempotent meaning Doing something multiple times has the same effect as doing it once.
Suppose you have an API: POST /createOrder?id=123

If the client accidentally sends the same request twice:

Idempotent: Only one order is created.
Non-idempotent: Two identical orders are created → bad.

### Relationship to Availability

- A system can be available but unreliable (responds with wrong data).
- A system can be reliable but unavailable (correct when up, but often down).
- Good systems aim for both.

---

### Key Idea

**Reliability answers:** _Does the system do the right thing over time?_

---

## 4. Fault Tolerance

Fault tolerance is the ability of a system to **continue operating even when components fail**.

Failures are expected in large systems and must be handled gracefully.

---

### Common Failures

- Server crashes.
- Disk failures.
- Network timeouts.
- Dependency outages.

---

### Practical Example

A distributed database stores data with three replicas:

- One node fails.
- Remaining nodes continue serving traffic.
- A new node joins and re-replicates data.
- Users do not notice the failure.

---

### Graceful Degradation

When full functionality isn’t possible:

- Cache fails → system falls back to database.
- Latency increases, but service remains usable.

---

### Fault Tolerance Techniques

- Replication and redundancy.
- Leader election and failover.
- Timeouts and retries (with limits).
- Circuit breakers to prevent cascading failures.
- Isolation between services.

---

### Key Idea

**Fault tolerance answers:** _What happens when something breaks?_

---

## 5. Latency vs Throughput

### Latency

Latency is the time it takes for **one request** to complete end-to-end.

**Example**
User clicks “Play” and video starts in 200 ms → latency = 200 ms.

---

### Throughput

Throughput is the **amount of work** the system can process per unit time.

**Example**
A streaming service delivers video to 100,000 users simultaneously → high throughput.

---

### Relationship and Trade-offs

- Low latency does not guarantee high throughput.
- High throughput systems may have higher latency.
- Batching, queues, and async processing:

  - Increase throughput.
  - Often increase latency.

---

### Practical Queue Example

- API enqueues a payment request and responds in 20 ms.
- During peak load, the queue grows.
- Payment confirmation arrives in 10 seconds.
- Result:

  - API latency is low.
  - End-to-end latency is high.
  - Throughput is high.

---

### Key Idea

- **Latency:** How fast is one operation?
- **Throughput:** How many operations can be handled?

---

## 6. Distributed Systems

A distributed system is a collection of **independent computers** that work together as a single system, communicating over a network.

---

### Architecture Example

An e-commerce system may have:

- Auth service
- Product catalog service
- Payment service
- Search service
- Cache layer
- Databases

Each runs on separate machines, possibly in different regions, but cooperates to serve one application.

---

### Benefits

- Scalability
- Fault tolerance
- High availability
- Geographic distribution (lower latency for users)

---

### Challenges

- Network latency.
- Partial failures.
- Data replication.
- Consistency vs availability trade-offs.
- Complex debugging and monitoring.

---

### Key Idea

Distributed systems enable modern scale, but introduce complexity that must be carefully managed.

---

## How These Concepts Fit Together

- **Scalability** allows the system to grow.
- **Availability** keeps the system reachable.
- **Reliability** ensures correctness.
- **Fault tolerance** keeps the system running during failures.
- **Latency vs throughput** defines performance trade-offs.
- **Distributed systems** are the foundation that enables all of the above at scale.

---

### Final Mental Model (Interview-Friendly)

- Scalability → _Can it grow?_
- Availability → _Is it up?_
- Reliability → _Is it correct?_
- Fault tolerance → _Does it survive failure?_
- Latency → _How fast?_
- Throughput → _How much at once?_
- Distributed systems → _How large systems are built_

---
