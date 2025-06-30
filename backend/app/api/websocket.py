from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def websocket_status():
    return {"status": "WebSocket endpoint coming soon"}
