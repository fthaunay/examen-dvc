import pandas as pd
from src.config_manager import DataTransformationConfig
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import os
from custom_logger import logger


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def normalisation(self) -> pd.DataFrame:
        
        # Normalisation X_train / X_test
        X_train = pd.read_csv(os.path.join(self.config.data_path, 'X_train.csv'))
        X_test = pd.read_csv(os.path.join(self.config.data_path, 'X_test.csv')) 

        scaler = StandardScaler()

        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.fit_transform(X_test) 

        pd.DataFrame(X_train_scaled).to_csv(
            os.path.join(self.config.data_path,
                         "X_train_scaled.csv"), index=False)
        pd.DataFrame(X_test_scaled).to_csv(
            os.path.join(self.config.data_path,
                         "X_test_scaled.csv"), index=False)

