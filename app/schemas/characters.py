from typing import Optional

from pydantic import BaseModel


class CharacterSchema(BaseModel):
    id: int
    name: str
    description: Optional[str]
    image: str
    role: str

    # add parse from SQLALchemy
    class Config:
        orm_mode = True


