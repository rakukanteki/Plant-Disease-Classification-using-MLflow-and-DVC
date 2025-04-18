from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"==========Stage {STAGE_NAME} has started===========")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"***********Stage {STAGE_NAME} is completed************")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"==========Stage {STAGE_NAME} has started===========")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f"***********Stage {STAGE_NAME} is completed************")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"==========Stage {STAGE_NAME} has started===========")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f"***********Stage {STAGE_NAME} is completed************")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f"==========Stage {STAGE_NAME} has started===========")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
    logger.info(f"***********Stage {STAGE_NAME} is completed************")
except Exception as e:
    logger.exception(e)
    raise e