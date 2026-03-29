from celery import Celery

celery_app = Celery(
    "viralgen",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

# IMPORTANT 👇
celery_app.autodiscover_tasks(["app.workers"])