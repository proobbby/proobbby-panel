# In your backend api/nodes.py (create this new route)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, auth, database

router = APIRouter()

@router.post("/nodes/register")
def register_node(node: schemas.NodeCreate, current_user=Depends(auth.get_current_user), db: Session = Depends(database.SessionLocal)):
    if not current_user.is_admin:
        raise HTTPException(403, "Admin access required")

    # Check if node exists, else create
    existing = crud.get_node_by_name(db, node.name)
    if existing:
        # update details if needed
        pass
    else:
        crud.create_node(db, node)
    return {"detail": "Node registered successfully"}
