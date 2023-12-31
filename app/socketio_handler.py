from .main import socket_manager as sm
@sm.on('/')
async def handle_join(sid, *args, **kwargs):
    await sm.emit('lobby', 'User joined')

@sm.on('leave')
async def handle_leave(sid, *args, **kwargs):
    await sm.emit('lobby', 'User left')

