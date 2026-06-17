from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

latest_command = "S"
clients = []


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

    global latest_command

    try:
        while True:
            data = await websocket.receive_text()

            latest_command = data.upper()

            print("Received:", data)
            print("Broadcasting:", latest_command)

            for client in clients:
                await client.send_text(latest_command)

    except:
        if websocket in clients:
            clients.remove(websocket)