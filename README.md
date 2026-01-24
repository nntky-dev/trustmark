# TrustMark



TrustMark is a minimal API that helps creators claim authorship of AI-generated or digital content by recording *who* claimed *what* and *when*.



This project is an early prototype designed to explore the idea of embedding "credit and trust" into generated content.



---



## What TrustMark Does



- Registers a claim for a piece of content (hashed)

- Records the author name and timestamp

- Verifies whether the same content has been claimed before

- Exposes a simple REST API for registration and verification



---



## What TrustMark Does NOT Do



- It does **not** prevent copying or screenshots

- It does **not** provide legal ownership or copyright enforcement

- It only supports *claim verification*, not *protection*



TrustMark is intended as a **deterrent and proof-assist tool**, not a security system.



---



## API Endpoints



### Health Check



```http

GET /health

