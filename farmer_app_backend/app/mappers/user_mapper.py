from app.models import User as User_Model
from app.helpers import User as User_Helper

class User_Mapper:

    @staticmethod
    def model_to_helper(model: User_Model) -> User_Helper:
        return User_Helper(
            id=model.id,
            user_name=model.user_name,
            password_hash=model.password_hash,
            roles=model.roles
        )

    @staticmethod
    def helper_to_model(helper: User_Helper) -> User_Model:
        return User_Model(
            id=helper.id,
            user_name=helper.user_name,
            password_hash=helper.password_hash,
            roles=helper.roles 
        )
