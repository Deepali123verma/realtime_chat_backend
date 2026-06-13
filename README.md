# 💬 Real-Time Chat Backend

A real-time chat backend built with **FastAPI**, **WebSockets**, **PostgreSQL**, and **Docker**. It enables instant messaging through WebSocket connections with secure and scalable backend architecture.

## 🚀 Features

- ⚡ Real-time messaging with WebSockets
- 🔐 User authentication
- 🗄 PostgreSQL + SQLAlchemy ORM
- 🧩 Clean modular architecture
- 🐳 Dockerized deployment
- 📘 Interactive API documentation (`/docs`)

## 🛠 Tech Stack

**FastAPI • Python • WebSockets • PostgreSQL • SQLAlchemy • Docker • Uvicorn**

## ⚙️ Setup

```bash
git clone https://github.com/Deepali123verma/realtime_chat_backend.git
cd realtime_chat_backend

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Server runs at:

```text
http://localhost:8000
```

## 📡 API Docs

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔌 WebSocket Endpoint

```text
ws://localhost:8000/ws
```

## 👩‍💻 Author

**Deepali Verma**

GitHub: `https://github.com/Deepali123verma`
