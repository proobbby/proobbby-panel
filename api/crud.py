def get_node_by_name(db: Session, name: str):
    return db.query(models.Node).filter(models.Node.name == name).first()

def create_node(db: Session, node: schemas.NodeCreate):
    db_node = models.Node(name=node.name, ip=node.ip, api_key=node.api_key)
    db.add(db_node)
    db.commit()
    db.refresh(db_node)
    return db_node
