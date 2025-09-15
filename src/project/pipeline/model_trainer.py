from src.project.components.model_trainer import ModelTrainer
from src.project.config.configuration import ConfigurationManager

STAGE_NAME = "Model training"

class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        try:
            configuarion_manager = ConfigurationManager()
            model_trainer_config = configuarion_manager.get_model_trainer_config()
            model_trainer = ModelTrainer(config = model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e