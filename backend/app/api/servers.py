from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database, auth

router = APIRouter()

@router.post("/", response_model=schemas.ServerRead)
def create_server(server: schemas.ServerCreate, current_user=Depends(auth.get_current_user), db: Session = Depends(database.SessionLocal)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admin can create servers")
    return crud.create_server(db, server, current_user.id)

@router.get("/", response_model=list[schemas.ServerRead])
def list_my_servers(current_user=Depends(auth.get_current_user), db: Session = Depends(database.SessionLocal)):
    return crud.get_servers_by_user(db, current_user.id)

@router.delete("/{server_id}")
def delete_server(server_id: int, current_user=Depends(auth.get_current_user), db: Session = Depends(database.SessionLocal)):
    server = crud.get_server_by_id(db, server_id)
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    if not current_user.is_admin and server.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")
    crud.delete_server(db, server_id)
    return {"detail": "Server deleted"}
