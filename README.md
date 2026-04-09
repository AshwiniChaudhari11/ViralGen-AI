# 🤖 ViralGen AI

Create viral marketing copy and stunning AI-generated images in seconds 🚀

---

## 📌 Overview

**ViralGen AI** is an AI-powered web application that helps users:

* ✍️ Generate marketing copy for different platforms
* 🎨 Create AI-generated images from text prompts
* ⚡ Get fast, asynchronous results using background workers

---

## 🏗️ Project Architecture

```
ViralGen AI
│
├── app/
│   ├── api/          # FastAPI route handlers (endpoints)
│   ├── services/     # Business logic (copy + image generation)
│   ├── agents/       # AI agents / prompt engineering logic
│   ├── workers/      # Background jobs (async image processing)
│   ├── models/       # Pydantic models / schemas
│   └── main.py       # FastAPI app entry point
│
├── static/           # Generated images storage
├── database/         # DB configs / job tracking
├── README.md         # Project documentation
```

---

## ⚙️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** FastAPI
* **AI Integration:** OpenAI / Stable Diffusion APIs
* **Async Processing:** Background workers / job queue
* **Database:** SQLite / PostgreSQL

---

## 🚀 Features

* ✅ AI Marketing Copy Generator
* ✅ Multi-platform support (Instagram, LinkedIn, Twitter)
* ✅ Tone selection (Professional, Witty, Urgent)
* ✅ AI Image Generation (Async)
* ✅ Image preview + download
* ✅ Job status tracking

---

## 🔄 Workflow

### ✍️ Copy Generation

1. User enters product description
2. Selects platform & tone
3. Backend generates optimized marketing copy
4. Result is displayed instantly

---

### 🎨 Image Generation (Async)

1. User enters image description
2. Request is sent to backend
3. Background worker processes image
4. Frontend polls job status
5. Image is displayed when ready

---

## 📡 API Endpoints

### Generate Copy

```
POST /generate-copy
```

### Generate Image (Async)

```
POST /generate-image-async
```

### Check Job Status

```
GET /job-status/{job_id}
```

---

## 🖥️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/viralgen-ai.git
cd viralgen-ai
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run Backend

```
uvicorn app.main:app --reload
```

### 4️⃣ Open Frontend

Open `index.html` in your browser

---


## 💡 Future Enhancements

* 🔐 User authentication
* 🕘 History of generated content
* 📊 Analytics dashboard
* 🌐 Deploy on cloud (AWS / Render / Vercel)

---


## ⭐ Contribute

Feel free to fork this repo and improve it!

---
