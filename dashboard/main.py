from fastapi import FastAPI, WebSocket
import asyncio, zmq, zmq.asyncio

app = FastAPI()
ctx = zmq.asyncio.Context()
sub = ctx.socket(zmq.SUB)
sub.connect("tcp://localhost:5556")
sub.setsockopt_string(zmq.SUBSCRIBE, "METRIC")

@app.get("/")
async def index():
    return FileResponse("dashboard/static/index.html")

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        topic, msg = await sub.recv_string().split(maxsplit=1)
        await ws.send_text(msg)          # broadcast metrics :contentReference[oaicite:12]{index=12}
        await asyncio.sleep(0.001)
