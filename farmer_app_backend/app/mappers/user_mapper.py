from app.models.user import User as User_Model
from app.helpers.user_helper import User as User_Helper


class User_Mapper:
#model_to_helper
     @staticmethod
     def model_to_helper(model:User_Model)->User_Helper:
          return User_Helper(
               id=model.id,
               user_name=model.user_name,
               password_hash=model.password_hash,
               role=model.role
          )
     
#helper_to_model
     @staticmethod
     def helper_to_model(helper:User_Helper)->User_Model:
          return User_Model(
               user_name=helper.user_name,
               password_hash=helper.password_hash,
               role=helper.role

          )





