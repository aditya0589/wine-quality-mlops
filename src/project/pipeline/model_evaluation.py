from src.project.components.model_evaluation import ModelEvaluation
from src.project.config.configuration import ConfigurationManager


STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.log_into_mlflow()
        except Exception as e:
            raise e