from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Users(Base):

    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    balance: Mapped[int] = mapped_column(server_default='0')
    password: Mapped[str]

