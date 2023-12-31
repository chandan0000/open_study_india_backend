
from fastapi import FastAPI, WebSocket
from sqlmodel import SQLModel
from fastapi.middleware.cors import CORSMiddleware
from .sockets import sio_app
# from fastapi_socketio import SocketManager

from .database import engine
from .router import auth, user

app = FastAPI()
SQLModel.metadata.create_all(engine)
# socket_manager = SocketManager(app=app)



app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# @app.get('/')
# async def home():
#     return {'message': 'Hello👋 Developers💻'}




# @app.websocket("/ws/{client_id}")
# async def websocket_endpoint(websocket: WebSocket, client_id: int):
#     await manager.connect(websocket)
#     try: 
#         while True:
#             data = await websocket.receive_text()
#             await manager.send_personal_message(f"You wrote: {data}", websocket)
#             await manager.broadcast(f"Client #{client_id} says: {data}")
#     except WebSocketDisconnect:
#         manager.disconnect(websocket)
#         await manager.broadcast(f"Client #{client_id} has left the chat")
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"Message text was: {data}")
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print("connedted user ", )
        await websocket.send_text(f"Message text was: {data}")

app.mount('/', app=sio_app)

        
app.include_router(auth.router)
app.include_router(user.router)



