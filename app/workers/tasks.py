from app.workers.celery_app import celery_app
from app.services.image_generator import generate_image


from app.services.job_service import save_job

@celery_app.task(bind=True)
def generate_image_task(self, product_description: str):

    image_url = generate_image(product_description)

    # SAVE RESULT IN DATABASE
    save_job(
        job_id=self.request.id,
        prompt=product_description,
        image_url=image_url,
        status="completed"
    )

    return {
        "status": "completed",
        "image_url": image_url
    }