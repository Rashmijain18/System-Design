- Scalability
  Scalability is how well a system can handle more load (users, data, requests) by adding more resources instead of rewriting everything.

  Vertical scaling (“scale up”) means giving a single machine more power: more CPU, RAM, or faster disks; this has limits because one machine can only grow so much.

  Horizontal scaling (“scale out”) means adding more machines and spreading traffic/data across them (load balancers, sharding, clustering), which is how large systems handle millions of users.

- Reliability
  Reliability is how consistently a system does the correct thing over time, even when parts fail.

  Reliable systems use redundancy: multiple instances, replicas of data, and health checks so if one node dies, another can take over with minimal impact.

  Techniques like automatic failover, backups, and monitoring help keep uptime high and reduce the chance of data loss or long outages.

- Distributed architectures/systems
  A distributed system is a set of independent computers that work together as if they were one system, communicating over a network.

  Components are split—e.g., separate services for auth, payments, search, caching—each running on its own machines, often in different regions, but cooperating to serve one application.

  Distributed systems bring benefits (scalability, fault tolerance, geo‑distribution) but also complexity: network latency, partial failures, data replication, and consistency problems must be carefully managed.
