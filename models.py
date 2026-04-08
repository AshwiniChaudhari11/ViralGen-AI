from db import jobs_collection
from datetime import datetime

def save_job(job_id, prompt, text, image_url, status):
    jobs_collection.insert_one({
        "job_id": job_id,
        "prompt": prompt,
        "generated_text": text,
        "image_url": image_url,
        "status": status,
        "created_at": datetime.utcnow()
    })