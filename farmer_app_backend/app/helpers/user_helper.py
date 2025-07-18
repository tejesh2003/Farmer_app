from typing import Optional, List
from app.models import Role 

class User:
    def __init__(
        self,
        user_name: str,
        password_hash: Optional[str] = "",
        roles: Optional[List[Role]] = None,
        id: Optional[str] = "",
    ):
        self.id = id
        self.user_name = user_name
        self.password_hash = password_hash
        self.roles = roles if roles else []

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_name": self.user_name,
            "roles": [role.name for role in self.roles],
            "password_hash": self.password_hash,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(
            id=data.get("id"),
            user_name=data["user_name"],
            password_hash=data.get("password_hash", ""),
            roles=data.get("roles", []),
        )
