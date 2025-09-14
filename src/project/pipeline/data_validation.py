from src.project.config.configuration import ConfigurationManager
from src.project.components.data_validation import DataValidation
from src.project.utils import logger

STAGE_NAME = "Data validation stage"

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_columns()


try:
    logger.info(f">>> stage {STAGE_NAME} started >>>")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed >>>")
except Exception as e:
    logger.exception(e)
    raise e
