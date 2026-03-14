from fastapi import FastAPI
from app.models.schemas import CopyRequest
from app.services.text_generator import generate_marketing_copy

app = FastAPI(title="ViralGen AI")

@app.get("/")
def home():
    return {"message": "ViralGen AI Week 1 Running"}

@app.post("/generate-copy")
def generate_copy(request: CopyRequest):

    result = generate_marketing_copy(
        request.product_description,
        request.platform,
        request.persona
    )

    return {
        "platform": request.platform,
        "persona": request.persona,
        "generated_copy": result
    }