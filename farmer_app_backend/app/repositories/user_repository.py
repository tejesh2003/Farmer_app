from app.models import User
from app.database import db
from app.mappers import User_Mapper 
from app.models import Role

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
        if not user_model:
           raise ValueError("User not found")
        return User_Mapper.model_to_helper(user_model)

    @staticmethod
    def get_user_count():
        return User.query.count()
    
    @staticmethod
    def update_user(user):
        user_model= User.query.filter_by(user_name=user.user_name).first()
        if not user_model:
           raise ValueError("User not found")

        new_roles = user.roles 
        if not isinstance(new_roles, list):
           raise ValueError("Roles must be provided as a list")
        resolved_roles = []
        for r in new_roles:
          if isinstance(r, Role):
            resolved_roles.append(r)
          elif isinstance(r, str):
            role_obj = Role.query.filter_by(name=r).first()
            if not role_obj:
                raise ValueError(f"Role '{r}' not found")
            resolved_roles.append(role_obj)
          else:
            raise TypeError(f"Unsupported role type: {type(r)}")
        user_model.roles = resolved_roles
        db.session.commit()
        user_helper= User_Mapper.model_to_helper(user_model)
        return user_helper