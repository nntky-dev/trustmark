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

## Architecture (Prototype)



This prototype uses a simple architecture focused on traceability rather than scalability.



- Client sends requests to FastAPI endpoints (`/register`, `/verify`)

- FastAPI runs inside a Docker container

- The container is deployed on AWS Lightsail

- Data is stored locally as `db.json` inside the container filesystem



This design makes it easy to understand where data is stored and how verification works.



### Future Ideas (Not Implemented)



- Replace Lightsail with ECS or AWS Lambda

- Replace `db.json` with DynamoDB

- Add authentication and access control

