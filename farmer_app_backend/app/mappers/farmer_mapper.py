from app.models.farmer import Farmer as Farmer_Model
from app.helpers.farmer_helper import Farmer as Farmer_Helper


class Farmer_Mapper:
#model_to_helper
     @staticmethod
     def model_to_helper(model:Farmer_Model)->Farmer_Helper:
          return Farmer_Helper(
               id=model.id,
               name=model.name,
               phone=model.phone,
               country_id=model.country_id,
               language=model.language,
          )
     
#helper_to_model
     @staticmethod
     def helper_to_model(helper:Farmer_Helper)->Farmer_Model:
          return Farmer_Model(
               name=helper.name,
               phone=helper.phone,
               country_id=helper.country_id,
               language=helper.language,
          )





