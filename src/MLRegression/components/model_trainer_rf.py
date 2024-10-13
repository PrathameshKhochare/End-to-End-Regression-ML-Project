import pandas as pd
import os
from MLRegression import logger
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import ElasticNet
import joblib
from MLRegression.config.configuration import RandomForestModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: RandomForestModelTrainerConfig):
        self.config = config


    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]


        rf = RandomForestRegressor(max_depth=self.config.max_depth,random_state=self.config.random_state, n_estimators=self.config.n_estimators,min_samples_split= self.config.min_samples_split)
        rf.fit(train_x, train_y)

        joblib.dump(rf, os.path.join(self.config.root_dir, "randomForest.joblib"))