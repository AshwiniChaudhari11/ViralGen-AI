# 🚀 ViralGen AI  
### Multi-Modal Social Media Ad Content Generator

**ViralGen AI** is an AI-powered marketing technology platform that generates complete social media campaign assets from a simple text brief.  
The system produces **platform-specific marketing copy** and **AI-generated visuals** while maintaining strict brand voice consistency and scalable processing.

---

## 📌 Project Overview

Marketing teams often need dozens of campaign variations daily.  
ViralGen AI automates this workflow by converting a short product description into a ready-to-use marketing asset.

**Input:**  
`"Red running shoes"`

**Output:**  
- Brand-controlled marketing copy  
- Enhanced image prompt  
- AI-generated promotional image  
- Unified campaign response

---

## 🎯 Core Features

### 🧠 Prompt Refinement Agent
Automatically enhances user prompts into high-quality image instructions for consistent visual generation.

### 🎙️ Brand Voice Enforcement
Marketing copy generated using predefined personas:
- Professional
- Witty
- Urgent
- Luxury
- Friendly
- Minimal

### ⚡ Asynchronous Processing
Image generation runs in background workers:
- API returns **Job ID instantly**
- Celery worker processes task
- Redis manages queue
- Polling endpoint retrieves results

### 🖼️ Multi-Modal Output
Combines AI text + generated image into a single campaign asset.

---

## 🏗️ Architecture


ViralGen AI
│
├── app/
│ ├── api/
│ ├── services/
│ ├── agents/
│ ├── workers/
│ ├── models/
│ └── main.py
│
├── static/ # Generated images
├── database/
└── README.md


---

## ⚙️ Tech Stack

- Python + FastAPI
- GPT-4 (Text Generation)
- Stability AI / DALL·E (Image Generation)
- Celery + Redis (Async Queue)
- MongoDB (Persistence)
- Pillow (Image Processing)
- Uvicorn Server

---

## 🔄 Workflow

1. User submits product brief  
2. Brand persona applied  
3. Marketing copy generated  
4. Prompt enhanced for visuals  
5. Async job created  
6. Image generated via worker  
7. Final asset returned via polling API  

---

## 📡 API Endpoints

### Generate Campaign
`POST /generate-campaign`

Returns:
```json
{
  "job_id": "123",
  "status": "processing"
}
Check Status

GET /job-status/{job_id}

Returns final marketing copy and image URL.

🧪 Implementation Timeline
Week 1: Text generation & brand personas
Week 2: Image generation pipeline
Week 3: Async queue system (Celery + Redis)
Week 4: Integration, persistence & end-to-end workflow
🚀 Installation
conda create -n viralgen python=3.10
conda activate viralgen
pip install -r requirements.txt

Create .env:

OPENAI_API_KEY=your_key
REDIS_URL=redis://localhost:6379
MONGODB_URI=your_mongodb_uri

Run services:

redis-server
celery -A app.workers.celery_worker worker --loglevel=info
uvicorn app.main:app --reload

Open API docs:

http://127.0.0.1:8000/docs
🎯 Use Cases
Marketing automation
Social media content generation
Startup branding tools
AI creative assistants