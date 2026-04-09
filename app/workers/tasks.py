# ✅ IMPORTS FIRST
from app.workers.celery_app import celery_app
from app.services.image_generator import generate_image
from app.services.job_service import save_job


# ✅ THEN DECORATOR
@celery_app.task(bind=True)
def generate_image_task(self, prompt):

    job_id = self.request.id

    filename = generate_image(prompt)

    BASE_URL = "http://127.0.0.1:8000"
    image_url = f"{BASE_URL}/static/generated/{filename}"

    save_job(job_id, prompt, image_url, "SUCCESS")

    return {
        "status": "success",
        "image_url": image_url
    }