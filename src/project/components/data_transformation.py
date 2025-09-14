import os
from project.entity.config_entity import DataTransformationConfig
from src.project.utils import logger
from sklearn.model_selection import train_test_split
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path, sep=";")

        train, test = train_test_split(data, test_size=0.2)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("spliited data into Training and Testing sets")
        logger.info(f"Training shape: {train.shape}")
        logger.info(f"Test shape {test.shape}")
        print(train.shape)
        print(test.shape)

        
