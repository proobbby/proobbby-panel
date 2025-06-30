from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, auth, database

router = APIRouter()

@router.post("/register")
def register_node(node: schemas.NodeCreate, current_user=Depends(auth.get_current_user), db: Session = Depends(database.SessionLocal)):
    if not current_user.is_admin:
        raise HTTPException(403, "Admin access required")
    existing = crud.get_node_by_name(db, node.name)
    if existing:
        # optionally update existing node details
        pass
    else:
        crud.create_node(db, node)
    return {"detail": "Node registered successfully"}
