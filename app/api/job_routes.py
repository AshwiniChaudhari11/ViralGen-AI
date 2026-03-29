from fastapi import APIRouter
from app.workers.tasks import generate_image_task
from celery.result import AsyncResult

router = APIRouter()

# submit job
@router.post("/generate-image-async")
def generate_async(prompt: dict):

    task = generate_image_task.delay(
        prompt["product_description"]
    )

    return {
        "job_id": task.id,
        "status": "processing"
    }


# check job status
@router.get("/job-status/{job_id}")
def job_status(job_id: str):

    task_result = AsyncResult(job_id)

    if task_result.state == "PENDING":
        return {"status": "pending"}

    elif task_result.state == "SUCCESS":
        return {
            "status": "completed",
            "result": task_result.result
        }

    return {"status": task_result.state}