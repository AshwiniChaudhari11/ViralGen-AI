from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.models.schemas import CopyRequest, ImageRequest
from app.services.text_generator import generate_marketing_copy
from app.services.image_generator import generate_image


app = FastAPI(title="ViralGen AI")

# ✅ Serve generated images
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return {"message": "ViralGen AI Week 2 Running"}


# -------- TEXT GENERATION --------
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


# -------- IMAGE GENERATION --------
@app.post("/generate-image")
def create_image(request: ImageRequest):

    result = generate_image(request.product_description)

    return {
        "original_prompt": request.product_description,
        "enhanced_prompt": result["enhanced_prompt"],
        "image_url": result["image_url"]
    }