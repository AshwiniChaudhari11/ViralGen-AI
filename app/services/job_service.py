from app.db.mongo import jobs_collection
from datetime import datetime


def save_job(job_id, prompt, image_url, status):

    jobs_collection.insert_one({
        "job_id": job_id,
        "prompt": prompt,
        "image_url": image_url,
        "status": status,
        "created_at": datetime.utcnow()
    })


def get_job(job_id):
    return jobs_collection.find_one({"job_id": job_id})