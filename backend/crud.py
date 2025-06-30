from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash

# ------------------------
# User CRUD
# ------------------------

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(db: Session):
    return db.query(models.User).all()

# ------------------------
# Server CRUD
# ------------------------

def create_server(db: Session, server: schemas.ServerCreate, user_id: int):
    db_server = models.Server(name=server.name, owner_id=user_id)
    db.add(db_server)
    db.commit()
    db.refresh(db_server)
    return db_server

def get_servers_by_user(db: Session, user_id: int):
    return db.query(models.Server).filter(models.Server.owner_id == user_id).all()

def get_server_by_id(db: Session, server_id: int):
    return db.query(models.Server).filter(models.Server.id == server_id).first()

def delete_server(db: Session, server_id: int):
    server = get_server_by_id(db, server_id)
    if server:
        db.delete(server)
        db.commit()
    return server
