# MOOD-API
A [RESTful API](#restful-api) for logging and managing daily moods. Built with [FastAPI](#fastapi) to practice backend development and clean API design.



## Words
### RESTful API
The API follows the <u>REST</u> architectural style.
- REST\
    REST (Representational State Transfer) is an architectural style for designing networked APIs. A RESTful API must follow six architectural constraints:
    1. Client-Server
    2. Stateless
    3. Cacheable
    4. Uniform Interface
    5. Layered System
    6. Code on Demand (optional)
- Other API Architectural Styles
    - RPC (Remote Procedure Call)\
        RPC defines a communication method where the client directly calls functions on the server.
    - GraphQL\
        GraphQL is a query language for APIs. The client specifies exactly which data it needs.
    - SOAP (Simple Object Access Protocol)\
        SOAP is a protocol that uses XML and follows strict, standardized rules.
    - gRPC (Google RPC)\
        gRPC is a high‑performance protocol using HTTP/2 and binary data formats.
    - WebSocket
        WebSocket provides a persistent, full‑duplex connection enabling real‑time communication.

### FastAPI