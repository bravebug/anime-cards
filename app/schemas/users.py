from pydantic import BaseModel


class UserSchemaRequest(BaseModel):
    username: str
    password: str


class UserSchemaResponse(BaseModel):
    id: int
    username: str
    balance: int

    # add parse from SQLALchemy
    class Config:
        orm_mode = True
