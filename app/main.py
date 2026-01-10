from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse

from app.database import Base, engine
from routers import users, rooms, messages, websocket_routes, auth_routers

# ------------------- Initialize FastAPI App -------------------
app = FastAPI(
    title="🚀 Real-Time Chat Backend",
    version="1.0.0",
    description="FastAPI-based real-time chat backend with JWT Authentication and WebSocket support."
)

# ------------------- Create DB Tables (SAFE WAY) -------------------
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

# ------------------- Include Routers -------------------
app.include_router(users.router)
app.include_router(rooms.router)
app.include_router(messages.router)
app.include_router(auth_routers.router)
app.include_router(websocket_routes.router)

# ------------------- Root Endpoint -------------------
@app.get("/")
@app.head("/")
def root():
    return {"message": "🚀 Welcome to the Real-Time Chat Backend! Visit /docs."}

# ------------------- Swagger JWT Authorize Button -------------------
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    for path in openapi_schema["paths"]:
        if path not in ["/auth/login", "/auth/register"]:
            for method in openapi_schema["paths"][path]:
                openapi_schema["paths"][path][method]["security"] = [
                    {"BearerAuth": []}
                ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

# ------------------- WebSocket Test Page -------------------
html = """
<!DOCTYPE html>
<html>
<head><title>FastAPI Chat</title></head>
<body>
<h1>💬 Real-Time Chat Using FastAPI WebSockets</h1>

<input type="text" id="username" placeholder="Enter your name" />
<button onclick="connectWS()">Connect</button>

<form id="form" style="margin-top:20px;">
    <input type="text" id="messageText" placeholder="Type message..." autocomplete="off"/>
    <button>Send</button>
</form>

<ul id="messages"></ul>

<script>
    let ws;

    function connectWS() {
        const name = document.getElementById("username").value;
        ws = new WebSocket(`ws://127.0.0.1:8000/ws/chat?username=${name}`);

        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            const msg = document.createElement('li');
            msg.textContent = `${data.sender}: ${data.message}`;
            messages.appendChild(msg);
        };
    }

    const form = document.getElementById('form');
    const input = document.getElementById('messageText');
    const messages = document.getElementById('messages');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        if (input.value.trim() !== "") {
            ws.send(input.value);
            input.value = '';
        }
    });
</script>
</body>
</html>
"""

@app.get("/chat", response_class=HTMLResponse)
def chat_page():
    return html
