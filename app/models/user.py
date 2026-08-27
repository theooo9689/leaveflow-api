from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import Boolean, DateTime, Enum, String, func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import SystemRole

if TYPE_CHECKING:
    from app.models.team_membership import TeamMembership


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )
    email: Mapped[str] = mapped_column(
        String(320),
        unique=True,
        index=True,
        nullable=False,
    )
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    system_role: Mapped[SystemRole] = mapped_column(
        Enum(
            SystemRole,
            name="system_role",
            values_callable=lambda enum_class: [role.value for role in enum_class],
        ),
        default=SystemRole.MEMBER,
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    memberships: Mapped[list[TeamMembership]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )
