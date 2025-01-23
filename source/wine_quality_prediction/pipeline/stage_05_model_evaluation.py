"""

"""

# Importing necessary libraries
from wine_quality_prediction.components.model_evaluation import ModelEvaluation
from wine_quality_prediction.config.configuration import ConfigurationManager
from wine_quality_prediction import logger

# Defining the ModelEvaluationPipeline Stage
STAGE_NAME = "STAGE 05: MODEL EVALUATION"

# Defining the ModelEvaluationPipeline class
class ModelEvaluationPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        try:
            # Instantiating the ConfigurationManager class
            config_manager = ConfigurationManager()
            # Getting the model evaluation configuration
            model_evaluation_config = config_manager.get_model_evaluation_config()
            # Instantiating the ModelEvaluation class
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            # Evaluating the model
            model_evaluation.log_in_mlflow()

        except Exception as e:
            logger.exception(e)
            raise e

# Running the ModelEvaluationPipeline
if __name__ == "__main__":
    try:
        logger.info(f">>>>> Starting {STAGE_NAME} <<<<<")
        ModelEvaluationPipeline.main()
        logger.info(f">>>>> Completed {STAGE_NAME} <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e