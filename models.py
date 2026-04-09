from app.db.db import jobs_collection
from datetime import datetime

def save_job(job_id, prompt, image_data, status):

    jobs_collection.insert_one({
        "job_id": job_id,
        "prompt": prompt,
        # store only URL string
        "image_url": image_data["image_url"],
        "enhanced_prompt": image_data["enhanced_prompt"],
        "status": status,
        "created_at": datetime.utcnow()
    })