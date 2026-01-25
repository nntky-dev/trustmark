from fastapi import FastAPI

from pydantic import BaseModel



from trustmark_v0 import register, verify



app = FastAPI(title="TrustMark API", version="0.1")





class RegisterRequest(BaseModel):

    name: str

    content: str





class VerifyRequest(BaseModel):

    content: str





@app.get("/health")

def health():

    return {"status": "ok"}





@app.post("/register")

def register_api(req: RegisterRequest):

    record = register(req.name, req.content)

    return {

        "status": "ok",

        "name": record["name"],

        "timestamp": record["timestamp"]

    }





@app.post("/verify")

def verify_api(req: VerifyRequest):

    h, matches = verify(req.content)

    if matches:

        r = matches[0]

        return {

            "status": "matched",

            "name": r["name"],

            "timestamp": r["timestamp"]

        }

    return {"status": "not_found"}

