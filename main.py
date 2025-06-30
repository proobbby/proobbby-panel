from fastapi import FastAPI
from app.api import auth, users, servers, websocket

app = FastAPI(title="Proobbby Panel API")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(servers.router, prefix="/servers", tags=["servers"])
app.include_router(websocket.router, prefix="/ws", tags=["websocket"])
