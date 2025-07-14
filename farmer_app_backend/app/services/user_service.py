from app.helpers.user_helper import User as UserHelper
from app.repositories.user_repository import UserRepository
from app.enums.role_enum import Role

class User_Service:

    @staticmethod
    def register_user(user_name:str, password_hash:str):

        count=UserRepository.get_user_count()
        
        if count==0:
            data= {
            "user_name":user_name,
            "password_hash" : password_hash,
            "role": Role.SUPER_USER,
            }
        else:
            data= {
            "user_name":user_name,
            "password_hash" : password_hash
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
    def update_user(user_name: str, role:str):

        user=User_Service.get_by_user_name(user_name)
        if not user:
           raise ValueError("User not found")
        
        user["role"]=role
        
        user_helper = UserHelper.from_dict(user)
        new_user_helper =UserRepository.update_user(user_helper)
        user_dict = UserHelper.to_dict(new_user_helper)
        user_dict.pop("password_hash")

        return user_dict


