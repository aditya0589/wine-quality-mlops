import pandas as pd
from src.project.entity.config_entity import ModelTrainerConfig
from sklearn.linear_model import ElasticNet
import os
import joblib


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        x_train = train_data.drop([self.config.target_column], axis=1)
        y_train = train_data[[self.config.target_column]]

        x_test = test_data.drop([self.config.target_column], axis = 1)
        y_test = test_data[[self.config.target_column]]

        elastic_model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state = 42)
        elastic_model.fit(x_train,y_train)

        joblib.dump(elastic_model, os.path.join(self.config.root_dir, self.config.model_name))


