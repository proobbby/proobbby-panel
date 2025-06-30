from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    is_admin: bool

    class Config:
        orm_mode = True

class ServerCreate(BaseModel):
    name: str

class ServerRead(BaseModel):
    id: int
    name: str
    status: str
    owner_id: int

    class Config:
        orm_mode = True
