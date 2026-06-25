from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class Program(Base):
    __tablename__ = "programs"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(255))

    platform: Mapped[str] = mapped_column(String(100))

    program_url: Mapped[str] = mapped_column(String(500))

    status: Mapped[str] = mapped_column(
        String(50),
        default="ACTIVE"
    )
