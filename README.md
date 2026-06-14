# 💬 Real-Time Chat Backend

A real-time chat backend built using **FastAPI**, **WebSockets**, **PostgreSQL**, and **Docker**. The application enables instant communication between users through WebSocket connections while providing secure authentication, room management, and persistent message storage.

---

## 🚀 Features

* ⚡ Real-time messaging with WebSockets
* 🔐 JWT-based user authentication
* 👥 User and chat room management
* 🗄 PostgreSQL integration with SQLAlchemy ORM
* 📦 RESTful APIs for users, rooms, and messages
* 🐳 Dockerized for easy deployment
* 📘 Interactive API documentation with Swagger (`/docs`)

---

## 🛠 Tech Stack

* **Backend:** FastAPI, Python
* **Database:** PostgreSQL, SQLAlchemy
* **Communication:** WebSockets
* **Authentication:** JWT
* **Deployment:** Docker
* **Server:** Uvicorn

---

## 📂 Project Structure

```text
realtime_chat_backend/
├── app/
│   ├── auth.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── websocket_manager.py
│
├── routers/
│   ├── auth_routers.py
│   ├── messages.py
│   ├── rooms.py
│   ├── users.py
│   └── websocket_routes.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

```bash
git clone https://github.com/DeepaliVerma/realtime_chat_backend.git
cd realtime_chat_backend

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## 📘 API Documentation

After starting the server, visit:

```text
http://localhost:8000/docs
```

to access the interactive Swagger UI.

---

## 👩‍💻 Author

**Deepali Verma**

GitHub: https://github.com/DeepaliVerma
