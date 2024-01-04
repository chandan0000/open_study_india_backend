import socketio

sio_server = socketio.AsyncServer(
    logger=True, 
    engineio_logger=True,
    async_mode='asgi',
    cors_allowed_origins=[]

)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    # socketio_path='socket.io'
)

# sio_server = socketio.Server()
# sio_app = socketio.WSGIApp(sio_server, )
@sio_server.event
async def connect(sid, environ, auth):
    print(f'{sid}: connected')
    await sio_server.emit('join', {'sid': sid})


@sio_server.event
async def chat(sid, message):
    await sio_server.emit('chat', {'sid': sid, 'message': message})


@sio_server.event
async def disconnect(sid):
    print(f'{sid}: disconnected')