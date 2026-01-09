## What is memory in a server?

When a server runs an application, it uses **RAM (Random Access Memory)** to temporarily store data it needs immediately.

- RAM is **fast but temporary**.
- If the server restarts, the RAM is cleared.
- Data stored in RAM is **not shared** with other servers.

---

## What is a session?

A **session** is a way for the server to remember who you are between requests.

For example, when you log in, the server saves your user ID and login status in memory (RAM) linked to your session ID.

Example:

```json
{
  "session_id": "abc123",
  "user_id": 1001,
  "logged_in": true,
  "cart_items": ["shoes", "hat"]
}
```

This session data is stored **in the RAM of the server that handled your login request**.

---

## What happens when there are multiple servers?

When your requests are sent through a load balancer distributing traffic across multiple servers, your requests can go to different servers each time.

Each server has its own RAM and session storage. So, if your first request goes to Server A, your session is saved in Server A’s memory.

If your next request goes to Server B, Server B does not have your session data, so it thinks you are not logged in.

---

## What is a sticky session?

Sticky session (also called **session affinity**) makes sure that once a user starts a session with one specific server, **all subsequent requests from that user go to the same server**.

This way, the server always has the session data in its own memory and can keep you logged in.

---

## How does the load balancer implement sticky sessions?

Usually with **cookies**:

- When you first connect, the load balancer sends a cookie like `SERVER_ID=server1`.
- Your browser sends this cookie with every request.
- The load balancer reads the cookie and routes your requests to the same server.

Alternatively, some load balancers use your **IP address** to route requests to the same server.

---

## Limitations of sticky sessions:

- If the server you are assigned to crashes, your session is lost.
- Difficult to scale because some servers might have more users than others.
- Session data in RAM is temporary and not shared between servers.
- Deploying or restarting servers causes session loss.

---

## Modern alternatives:

Instead of sticky sessions, sessions are stored in:

- A shared **Redis** cache
- A **database**
- Or use **stateless tokens (JWT)**

This allows **any server to handle any request** because session data is shared or encoded in tokens.
Best practice (IMPORTANT)

❗ Avoid sticky sessions in modern systems
