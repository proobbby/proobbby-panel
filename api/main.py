from app.api import nodes
app.include_router(nodes.router, prefix="/nodes", tags=["nodes"])
