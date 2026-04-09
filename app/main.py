from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.models.schemas import CopyRequest, ImageRequest
from app.services.text_generator import generate_marketing_copy
from app.workers.tasks import generate_image_task
from celery.result import AsyncResult
from app.services.job_service import get_job
from app.workers.celery_app import celery_app

app = FastAPI(title="ViralGen AI")

# ✅ Static files (CSS + JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ Templates folder
templates = Jinja2Templates(directory="templates")


# ---------- FRONTEND ROUTE ----------
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


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


# -------- IMAGE ASYNC --------
@app.post("/generate-image-async")
def create_image_async(request: ImageRequest):

    task = generate_image_task.delay(request.product_description)

    return {
        "message": "Image generation started",
        "job_id": task.id
    }


# -------- JOB STATUS --------
@app.get("/job-status/{job_id}")
def get_job_status(job_id: str):

    job = get_job(job_id)

    # ✅ If stored in DB / Redis
    if job:
        return {
            "status": job["status"],
            "image_url": job.get("image_url")  # return directly
        }

    # ✅ Check Celery task state
    task_result = AsyncResult(job_id, app=celery_app)

    if task_result.state == "PENDING":
        return {"status": "pending"}

    elif task_result.state == "FAILURE":
        return {
            "status": "failed",
            "error": str(task_result.info)
        }

    elif task_result.state == "SUCCESS":
        return {
            "status": "completed",
            "image_url": task_result.result
        }

    return {"status": task_result.state}