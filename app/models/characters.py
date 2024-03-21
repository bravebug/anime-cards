from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Characters(Base):

    __tablename__ = 'characters'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
    image: Mapped[str]
    role: Mapped[str]
