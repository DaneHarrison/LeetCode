4. APIs & Integration
   Shopify's developer platform is heavily GraphQL.

GraphQL vs. REST for a public merchant API: why did Shopify go GraphQL, and what problems does it introduce (query cost, N+1, caching)?
How does a DataLoader/promise-batching pattern solve N+1 in a GraphQL resolver?
Design rate limiting for a public API: fixed window vs. token bucket vs. sliding window. What breaks under distributed deployments?
How do you design a webhook delivery system with at-least-once delivery, retries with backoff, and idempotent consumers?
How would you version a public API without breaking thousands of third-party apps?
Explain idempotency keys: where do they go, what do you store, and what happens on retry?
How would you design pagination for a dataset that changes while the client pages through it (cursor-based)?
An integration partner sends malformed payloads 0.1% of the time. Design the ingestion pipeline so nothing is silently lost. 4. Technical Deep Dive (Past Projects)
Conversational — pick 1–2 projects you owned end-to-end.

Walk me through a system you designed at your last job. How does every part work?
What was the business impact of that project? How did you measure it?
What alternatives did you consider for [key architectural decision], and why did you choose this one?
What's the biggest mistake or trade-off you made in that project? What would you do differently today?
What was the hardest bug or failure you hit in that project, and how did you debug it?
What's the most interesting technical problem hidden in that system?
How did you collaborate with product, design, or other teams to ship it?
How would this system behave at 10x the scale? 5. System Design (Commerce-Flavored)
Shopify anchors design problems in real merchant scenarios — always reason through the merchant impact.

Design a checkout system that survives Black Friday / Cyber Monday — 10–40x normal traffic, with single hero merchants spiking into hundreds of thousands of orders per minute.
Design an inventory management system that prevents overselling across multiple warehouses and sales channels.
Design the path from "customer clicks checkout" to "settled charge" such that no charge is lost or duplicated, even when a payment processor is timing out. (Probe: idempotency keys, retries, exactly-once semantics.)
Design a multi-tenant platform serving millions of storefronts where one merchant's viral spike can't degrade another merchant's experience.
Design a webhook delivery platform guaranteeing at-least-once delivery for merchant apps.
Design a flash-sale system for a limited product drop — how do you prevent the thundering herd on inventory?
How would you architect feature flags for a gradual rollout to millions of stores?
Walk through migrating a critical system with zero downtime.
Design a merchant analytics dashboard with reasonable latency over billions of events.
For any of the above: "During a flash sale, degraded search is acceptable but a broken checkout is not — how does your design reflect that?" 3. Coding & Pair Programming
Done live in the candidate's own IDE, 75–90 minutes, with progressively layered requirements.

Hands-on exercises:

Implement a rate limiter for webhook deliveries.
Build a shipping rate calculator; then add fragile-item surcharges, multi-package splitting, and expiring regional discounts layer by layer.
Implement a pricing engine with discount stacking rules (e.g., automatic + code stack; two codes don't).
Design an inventory reservation system that prevents two shoppers from buying the last item simultaneously.
Implement a Datasource class that supports lazy .map().filter().collect() chaining.
Extend an existing checkout model to support gift cards or product bundles.
Implement a cache with expiration and preemptive refresh.
Calculate total order value with discounts, tax, and multi-currency support.
