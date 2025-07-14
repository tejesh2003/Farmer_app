from app.models.user import User
from app.database import db
from app.mappers.user_mapper import User_Mapper 
from app.enums.role_enum import Role

class UserRepository:

    @staticmethod
    def save_user(user):
        user_model=User_Mapper.helper_to_model(user)
        db.session.add(user_model)
        db.session.commit()
        user_helper=User_Mapper.model_to_helper(user_model)
        return user_helper

    @staticmethod
    def user_exists_by_user_name(user_name):
        return User.query.filter_by(user_name = user_name).first() is not None
    
    @staticmethod
    def get_by_user_name(user_name):
        user_model= User.query.filter_by(user_name=user_name).first()
        return User_Mapper.model_to_helper(user_model)

    @staticmethod
    def get_user_count():
        return User.query.count()
    
    @staticmethod
    def update_user(user):
        user_model= User.query.filter_by(user_name=user.user_name).first()
        if not user_model:
           raise ValueError("User not found")

        new_role = user.role if isinstance(user.role, Role) else Role[user.role]
        user_model.role = new_role
        db.session.commit()
        user_helper= User_Mapper.model_to_helper(user_model)
        return user_helper