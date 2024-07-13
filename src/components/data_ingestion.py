import pandas as pd
import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts/ingested_data", "train.csv")
    test_data_path: str = os.path.join("artifacts/ingested_data", "test.csv")
    row_data_path: str = os.path.join("artifacts/ingested_data", "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion method or component.")
        try:
            df = pd.read_csv("artifacts/data_cleaned/cars24_cleaned.csv", index_col=0)
            logging.info("Successfully read dataset as dataframe.")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.row_data_path, index=False)

            logging.info("Train test split initiated.")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("Data ingestion completed.")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    data_ingestion_obj = DataIngestion()
    train_data_path, test_data_path = data_ingestion_obj.initiate_data_ingestion()

    data_transformation_obj = DataTransformation()
    train_data_transformed, test_data_transformed, _ = data_transformation_obj.initiate_data_transformation(train_data_path, test_data_path)

    model_trainer_obj = ModelTrainer()
    model_trainer_obj.initiate_model_training(train_data_transformed, test_data_transformed)