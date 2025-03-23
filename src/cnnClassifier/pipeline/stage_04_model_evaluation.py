from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_evaluation_mlflow import Evaluation
from src.cnnClassifier import logger

STAGE_NAME = "Model Evaluation"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f"><><><><><><><><><><><><><><><><><><><")
        logger.info(f"===========Stage {STAGE_NAME} has started===========")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f"--------Stage {STAGE_NAME} is completed--------")
    except Exception as e:
        logger.exception(e)
        raise e