import sys
import os
from src.project.pipeline.model_evaluation import ModelEvaluationPipeline
from src.project.pipeline.model_trainer import ModelTrainerPipeline
from src.project.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.project.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.project.pipeline.data_validation import DataValidationTrainingPipeline
from src.project.utils import logger

STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f">>> stage {STAGE_NAME} started >>>")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed >>>")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data validation stage"
try:
    logger.info(f">>> Stage {STAGE_NAME} started >>>")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed >>>")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation"
try:
    logger.info(f">>> Stage {STAGE_NAME} started")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed >>>")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model trainer"

try:
    logger.info(f">>> Stage {STAGE_NAME} started")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f">>> Stage {STAGE_NAME} completed >>>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation"
try:
    logger.info(f">>> Stage {STAGE_NAME} started >>>")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>> Stage {STAGE_NAME} completed >>>")
except Exception as e:
    logger.exception(e)
    raise e







    