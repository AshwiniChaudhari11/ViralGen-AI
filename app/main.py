from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.models.schemas import CopyRequest, ImageRequest
from app.services.text_generator import generate_marketing_copy
from app.services.image_generator import generate_image
from app.workers.tasks import generate_image_task
from celery.result import AsyncResult
from app.workers.celery_app import celery_app
from app.api.job_routes import router as job_router
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


@app.post("/generate-image-async")
def create_image_async(request: ImageRequest):

    task = generate_image_task.delay(request.product_description)

    return {
        "message": "Image generation started",
        "job_id": task.id
    }
@app.get("/job-status/{job_id}")
def get_job_status(job_id: str):

    task_result = AsyncResult(job_id, app=celery_app)

    if task_result.state == "PENDING":
        return {"status": "pending"}

    elif task_result.state == "SUCCESS":
        return task_result.result

    elif task_result.state == "FAILURE":
        return {
            "status": "failed",
            "error": str(task_result.info)
        }

    return {"status": task_result.state}