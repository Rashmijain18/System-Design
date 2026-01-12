 What is a Proxy?
A proxy is an intermediate machine that sits between two parties and passes messages between them.

Instead of:

Client  →  Server

It becomes:

Client  →  Proxy  →  Server

The proxy:

Receives a request
Decides what to do with it
Forwards it (or blocks / modifies it)
Receives the response
Sends the response back

Why a proxy exists at all

Because having a middle layer allows:
Control
Security
Visibility
Performance optimization

Without a proxy, the client and server must trust and talk to each other directly.

---

4. Forward Proxy (Client-side Proxy)

A forward proxy represents the client.

The client knows about the proxy and explicitly uses it.

Client → Forward Proxy → Internet Server

Who controls it?

The client

Or the organization/network the client belongs to


What problem it solves

Control what clients can access

Hide client identity

Centralize outbound traffic

---

How it works step-by-step

1. Client wants to access google.com
2. Client sends request to the proxy, not to Google
3. Proxy sends request to Google
4. Google responds to proxy
5. Proxy returns response to client

Google sees:
Request coming from Proxy IP
Not the client’s IP.

---

What forward proxy is typically used for

✅ Internet access control
✅ Blocking websites
✅ Monitoring employee traffic
✅ Client anonymity
✅ Caching external resources

---

Example: Corporate network

Employee Laptop
   |
   | (All traffic forced)
   v
Forward Proxy (Firewall / Squid)
   |
   v
Internet

You cannot bypass it
All requests are logged
Some domains are blocked

---

5. Reverse Proxy (Server-side Proxy)
A reverse proxy represents the server.
Clients do not know they are talking to a proxy
Client → Reverse Proxy → Backend Server(s)

---

Who controls it?
The server owner
Infrastructure / DevOps team

---

How it works step-by-step

1. Client sends request to api.example.com
2. DNS points to reverse proxy
3. Reverse proxy receives request
4. Reverse proxy decides:
Which backend server
Whether to cache
Whether request is allowed
5. Backend responds to proxy
6. Proxy sends response to client

Client thinks:

"I talked directly to example.com"

But actually:

example.com → Reverse Proxy → Internal servers

---

What reverse proxy is typically used for

✅ Load balancing
✅ SSL termination
✅ Security (hide backend IPs)
✅ Rate limiting
✅ Caching
✅ Central auth / logging

---

Example: Web application

Users
  |
  v
Reverse Proxy (Nginx / Envoy)
  |
  +--> App Server 1
  +--> App Server 2
  +--> App Server 3

No user can directly reach the app servers.
