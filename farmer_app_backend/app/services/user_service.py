from app.helpers import User as UserHelper
from app.repositories import UserRepository
from app.models import Role

class User_Service:

    @staticmethod
    def register_user(user_name: str, password_hash: str):
        count = UserRepository.get_user_count()

        role_name = "SUPER_USER" if count == 0 else "USER"
        role_obj = Role.query.filter_by(name=role_name).first()

        if not role_obj:
            raise ValueError(f"Role '{role_name}' not found.")

        data = {
            "user_name": user_name,
            "password_hash": password_hash,
            "roles": [role_obj],
        }

        user_helper = UserHelper.from_dict(data)
        new_user_helper = UserRepository.save_user(user_helper)
        user_dict = UserHelper.to_dict(new_user_helper)
        user_dict.pop("password_hash")

        return user_dict
    
    @staticmethod
    def get_by_user_name(user_name:str):

        user_helper= UserRepository.get_by_user_name(user_name)

        return UserHelper.to_dict(user_helper)
    
    @staticmethod
    def add_user(user_name: str, role:Role):

        user=User_Service.get_by_user_name(user_name)
        if not user:
           raise ValueError("User not found")
        
        current_roles = user.get("roles", [])
        if role.name not in current_roles:
           current_roles.append(role.name)

        user["roles"] = current_roles
        
        user_helper = UserHelper.from_dict(user)
        new_user_helper =UserRepository.update_user(user_helper)
        user_dict = UserHelper.to_dict(new_user_helper)
        user_dict.pop("password_hash")
        return user_dict
    
    @staticmethod
    def remove_user(user_name: str, role:Role):

        user=User_Service.get_by_user_name(user_name)
        if not user:
           raise ValueError("User not found")
        
        current_roles = user.get("roles", [])
        updated_roles = [r for r in current_roles if r != role.name]

        if not updated_roles:
            raise ValueError("User must have at least one role assigned")

        user["roles"] = updated_roles
        user_helper = UserHelper.from_dict(user)
        new_user_helper =UserRepository.update_user(user_helper)
        user_dict = UserHelper.to_dict(new_user_helper)
        user_dict.pop("password_hash")
        return user_dict
    
    @staticmethod
    def get_all_users():
        user_helpers = UserRepository.get_all_users()
        if not user_helpers:
            return []

        users = []
        for helper in user_helpers:
            user_dict = UserHelper.to_dict(helper)
            user_dict.pop("password_hash", None)
            users.append(user_dict)

        return users



