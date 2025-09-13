from src.project.config.configuration import ConfigurationManager
from src.project.components.data_ingestion import DataIngestion
from src.project.utils import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config = data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e

try:
    logger.info(f">>> stage {STAGE_NAME} started >>>")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed >>>")
except Exception as e:
    logger.exception(e)
    raise e





