from enum import StrEnum


class SystemRole(StrEnum):
    MEMBER = "member"
    ADMIN = "admin"


class MembershipRole(StrEnum):
    MEMBER = "member"
    MANAGER = "manager"
