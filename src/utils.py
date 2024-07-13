import os
import sys
import pandas as pd
import numpy as np
import dill
from sklearn.metrics import r2_score

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_model(x_train, y_train, x_test, y_test, models):
    try:
        report = {}

        for model_name in models:
            model = models[model_name]
            model.fit(x_train, y_train)

            y_train_predict = model.predict(x_train)
            y_test_predict = model.predict(x_test)

            train_model_score = r2_score(y_train, y_train_predict)
            test_model_score = r2_score(y_test, y_test_predict)

            print(f"\n{model_name}")
            print(f"{train_model_score}")
            print(f"{test_model_score}")

            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise CustomException(e, sys)