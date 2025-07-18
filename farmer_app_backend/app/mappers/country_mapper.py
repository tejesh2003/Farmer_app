from app.models import Country as Country_Model
from app.helpers import Country as Country_Helper


class Country_Mapper:
#model_to_helper
     @staticmethod
     def model_to_helper(model:Country_Model)->Country_Helper:
          return Country_Helper(
               id=model.id,
               country_name=model.country_name,
               farmers=model.farmers
          )
     
#helper_to_model
     @staticmethod
     def helper_to_model(helper:Country_Helper)->Country_Model:
          return Country_Model(
               country_name=helper.country_name,
               id=helper.id,
               farmers=helper.farmers
          )





