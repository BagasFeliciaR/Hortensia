from datetime import datetime

from sqlalchemy import Boolean, DateTime, JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True)

    type: Mapped[str] = mapped_column(String(100))

    status: Mapped[str] = mapped_column(
        String(30),
        default="PENDING",
    )

    payload: Mapped[dict] = mapped_column(JSON)

    approval_required: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    approved: Mapped[bool | None] = mapped_column(
        Boolean,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    finished_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    error: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )
