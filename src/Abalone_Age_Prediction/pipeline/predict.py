import numpy as np
import pandas as pd
from Abalone_Age_Prediction.utils.common import load_object
import os
from pathlib import Path



class PredictPipeline:
    def __init__(self):
        pass
        
    def predict(self,features):
   
        model_path = Path('artifacts/best_model/best_model.pkl')
        model = load_object(file_path = model_path)
        prediction = model.predict(features)
        return prediction
    
        

class CustomData:
    def __init__(self, Sex:str, Length:float, Diameter:float,
                 Height:float, Whole_weight:float,Shucked_weight:float,Viscera_weight:float,Shell_weight:float):
        
        self.Sex = Sex
        self.Length = Length
        self.Diameter = Diameter
        self.Height = Height
        self.Whole_weight = Whole_weight
        self.Shucked_weight = Shucked_weight
        self.Viscera_weight = Viscera_weight
        self.Shell_weight = Shell_weight

    def get_data_as_data_frame(self):
        custom_data_input_dict = {
                "Sex" : [self.Sex],
                "Length" : [self.Length],
                "Diameter" : [self.Diameter],
                "Height" : [self.Height],
                "Whole weight" : [self.Whole_weight],
                "Shucked weight" : [self.Shucked_weight],
                "Viscera weight" : [self.Viscera_weight],
                "Shell weight" : [self.Shell_weight],
            }

        return pd.DataFrame(custom_data_input_dict)
        
