import os
import pandas as pd
import joblib
from sklearn.linear_model import ElasticNet
from src.entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        X_train = pd.read_csv(self.config.X_train_path)
        y_train = pd.read_csv(self.config.y_train_path)


        import pickle

        # open a file, where you stored the pickled data
        with open(os.path.join(self.config.root_dir, self.config.params_file), 'rb') as file: 
        # dump information to that file
            lr = pickle.load(file)
          
            lr.fit(X_train, y_train)

            joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))