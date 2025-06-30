from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database, auth

router = APIRouter()

@router.get("/me", response_model=schemas.UserRead)
def get_my_profile(current_user: schemas.UserRead = Depends(auth.get_current_user)):
    return current_user

@router.get("/", response_model=list[schemas.UserRead])
def list_users(current_user=Depends(auth.get_current_user), db: Session = Depends(database.SessionLocal)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")
    return crud.get_all_users(db)
