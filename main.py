from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"==========Stage {STAGE_NAME} has started===========")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"***********Stage {STAGE_NAME} is completed************")
except Exception as e:
    logger.exception(e)
    raise e