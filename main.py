import sys
import os
from src.project.pipeline.data_ingestion import DataIngestionTrainingPipeline
# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from project.utils import logger

STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f">>> stage {STAGE_NAME} started >>>")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed >>>")
except Exception as e:
    logger.exception(e)
    raise e







    