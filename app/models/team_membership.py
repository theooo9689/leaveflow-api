from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Enum, ForeignKey, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import MembershipRole

if TYPE_CHECKING:
    from app.models.team import Team
    from app.models.user import User


class TeamMembership(Base):
    __tablename__ = "team_memberships"
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "team_id",
            name="uq_team_memberships_user_id_team_id",
        ),
    )

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    team_id: Mapped[UUID] = mapped_column(
        ForeignKey("teams.id", ondelete="CASCADE"),
        nullable=False,
    )
    role: Mapped[MembershipRole] = mapped_column(
        Enum(
            MembershipRole,
            name="membership_role",
            values_callable=lambda enum_class: [role.value for role in enum_class],
        ),
        default=MembershipRole.MEMBER,
        nullable=False,
    )
    joined_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    user: Mapped[User] = relationship(back_populates="memberships")
    team: Mapped[Team] = relationship(back_populates="memberships")
