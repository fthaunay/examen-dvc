import os
import pandas as pd
import joblib
from sklearn.linear_model import ElasticNet
from src.entity import GridSearchConfig
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso, Ridge
import pickle 


class ModelGridSearch:
    def __init__(self, config: GridSearchConfig):
        self.config = config

    def define(self):
        X_train = pd.read_csv(self.config.X_train_path)
        y_train = pd.read_csv(self.config.y_train_path)

        parameters = {'alpha': [1, 10]}

        # define the model/ estimator
        model = Ridge()

        # define the grid search
        Ridge_reg = GridSearchCV(model, parameters,
                                 scoring='neg_mean_squared_error',
                                 cv=5)

        Ridge_reg.fit(X_train, y_train)

        # best estimator
        print(Ridge_reg.best_estimator_)
        
        with open(os.path.join(self.config.root_dir, self.config.params_file), 'wb') as file: 
            pickle.dump(Ridge_reg.best_estimator_, file) 
 
