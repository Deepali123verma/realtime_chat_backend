from fastapi import APIRouter, WebSocket
from app.websocket_manager import WebSocketManager

router = APIRouter()
manager = WebSocketManager()

@router.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):

    # STEP 1: Read username from connection URL
    username = websocket.query_params.get("username", "Unknown")

    # STEP 2: Connect the user with their name
    await manager.connect(websocket, username)

    try:
        while True:
            message = await websocket.receive_text()

            # STEP 3: Broadcast message with sender name
            await manager.broadcast({
                "sender": username,
                "message": message
            })

    except Exception:
        manager.disconnect(websocket)
