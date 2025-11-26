# app/websocket_manager.py

from typing import List, Dict
from fastapi import WebSocket

class WebSocketManager:
    def __init__(self):
        self.active_connections: List[Dict] = []
        # [{"socket": ws, "username": "Deepali"}]

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections.append({
            "socket": websocket,
            "username": username
        })

    def disconnect(self, websocket: WebSocket):
        self.active_connections = [
            conn for conn in self.active_connections
            if conn["socket"] != websocket
        ]

    async def broadcast(self, data: dict):
        for conn in self.active_connections:
            await conn["socket"].send_json(data)
