Health Checks
Why health checks are needed

Load balancers must not send traffic to dead or unhealthy servers.

Without health checks:

LB → Server A (DOWN) ❌
LB → Server B (UP) ✅

Users get errors even though healthy servers exist.

What is a health check?

A periodic request sent by the load balancer to each backend server to determine:

Is the server alive?

Is the app functioning correctly?

Types of Health Checks
1️⃣ L4 (Transport-level)

Checks TCP connection only.

Example:

“Can I open TCP connection on port 80?”

SYN → ACK → OK

✅ Very fast
❌ App may be broken but port is open

2️⃣ L7 (Application-level) ⭐ MOST USED

LB sends an HTTP request:

GET /health

Server responds:

{
"status": "ok",
"db": "connected",
"cache": "ok"
}

LB decides:

200 → healthy

500 → unhealthy

Health Check Parameters (IMPORTANT)
✔ Interval

How often to check:

every 5 seconds

✔ Timeout

How long to wait:

timeout 2s

✔ Healthy threshold

How many successes before marking healthy:

2 consecutive successes

✔ Unhealthy threshold

How many failures before marking unhealthy:

3 consecutive failures

Example (NGINX)
location /health {
return 200 "OK";
}

Upstream config:

server app1 max_fails=3 fail_timeout=30s;

Advanced Health Checks
🔹 Readiness vs Liveness (Kubernetes)

Liveness → is the process alive?

Readiness → can it accept traffic?

Example:

DB down → liveness = OK, readiness = FAIL

What happens when a server fails?

Health check fails

LB marks server unhealthy

Traffic stops going to that server

When healthy again → traffic resumes

This is automatic fault tolerance
