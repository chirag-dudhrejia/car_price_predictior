import os
import sys
import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            preprocessor_path="artifacts/transformed_files/car_preprocessor.pkl"
            model_path = "artifacts/model_train_files/model.pkl"

            preprocessor = load_object(file_path=preprocessor_path)
            model = load_object(file_path=model_path)

            scaled_features = preprocessor.transform(features)
            prediction = model.predict(scaled_features)

            return prediction
        except Exception as e:
            raise CustomException(e, sys)



class CustomData:
    def __init__(self, Car_name: str, Year: int, Distance: int, Fuel_type: str, Drive: str):
        self.car_name = Car_name
        self.year = Year
        self.distance = Distance
        self.fuel_type = Fuel_type
        self.drive = Drive

    def get_data_as_dataframe(self):
        try:
            custom_data_dict = {
                "Car_name": [self.car_name],
                "Year": [self.year],
                "Distance": [self.distance],
                "Fuel_type": [self.fuel_type],
                "Drive": [self.drive]
            }

            return pd.DataFrame(custom_data_dict)
        except Exception as e:
            raise CustomException(e, sys)