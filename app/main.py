
from fastapi import FastAPI, WebSocket
from sqlmodel import SQLModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
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
app.include_router(auth.router)
app.include_router(user.router)

@app.get('/')
async def home():
    return {'message': 'Hello👋 Developers💻'}


app.mount('/', app=sio_app)

        



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

