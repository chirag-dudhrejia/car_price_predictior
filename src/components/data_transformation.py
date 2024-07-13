import sys
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts/transformed_files", "car_preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_obj(self):
        '''
        This Function is responsible for data transformation
        '''

        try:
            numeric_columns = ["Year", "Distance"]
            categoric_columns = ["Car_name", "Fuel_type", "Drive"]

            num_pipeline=Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            whole_data = pd.read_csv("artifacts/ingested_data/data.csv")
            ohe = OneHotEncoder()
            ohe.fit(whole_data[["Car_name", "Fuel_type", "Drive"]])

            cat_pipeline=Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("ohe", OneHotEncoder(categories=ohe.categories_))
                ]
            )

            logging.info(f"Created transformer pipeline for numeric columns: {numeric_columns}")
            logging.info(f"Created transformer pipeline for categoric columns: {categoric_columns}")

            preprocessor = ColumnTransformer([
                ("numeric_pipeline", num_pipeline, numeric_columns),
                ("categoric_pipeline", cat_pipeline, categoric_columns)
            ])

            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed.")

            logging.info("Obtaining preprocessing object.")
            preprocessing_obj = self.get_data_transformer_obj()

            target_column_name = "Price"

            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on training dataframe and testing dataframe.")

            input_features_train_arr = preprocessing_obj.fit_transform(input_feature_train_df).toarray()
            input_features_test_arr = preprocessing_obj.transform(input_feature_test_df).toarray()

            train_arr = np.c_[input_features_train_arr, target_feature_train_df.to_numpy()]
            test_arr = np.c_[input_features_test_arr, target_feature_test_df.to_numpy()]

            logging.info("Successfully Applied preprocessing object on training dataframe and testing dataframe.")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            logging.info("Saved preprocessing object.")

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e, sys)