from typing import Optional
from app.enums.role_enum import Role

class User:
    def __init__(
        self,
        id : Optional[str] ="",
        user_name : str = "",
        password_hash : Optional[str] = "",
        role: Role = Role.USER,
    ):
        self.id=id
        self.user_name=user_name
        self.password_hash=password_hash
        self.role=role

    def to_dict(self)->dict:
        return {
            "id" : self.id,
            "user_name" : self.user_name,
            "role" : self.role.name,
            "password_hash" : self.password_hash
        }
    
    @staticmethod
    def from_dict(data: dict):
       role = Role[data["role"]] if "role" in data else Role.USER
       return User(
           user_name=data["user_name"],
           password_hash=data["password_hash"],
           role=role
        )
    
        