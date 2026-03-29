from app.workers.celery_app import celery_app
from app.services.image_generator import generate_image


@celery_app.task(bind=True)
def generate_image_task(self, product_description: str):

    result = generate_image(product_description)

    return {
        "status": "completed",
        "original_prompt": product_description,
        "enhanced_prompt": result["enhanced_prompt"],
        "image_url": result["image_url"]
    }