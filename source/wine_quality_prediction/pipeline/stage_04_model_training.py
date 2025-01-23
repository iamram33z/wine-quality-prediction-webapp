"""
Pipeline Stage for Model Training
"""

#  Importing necessary libraries
from wine_quality_prediction.components.model_training import ModelTraining
from wine_quality_prediction.config.configuration import ConfigurationManager
from wine_quality_prediction import logger

# Defining the ModelTrainingPipeline Stage
STAGE_NAME = "STAGE 04: MODEL TRAINING"

# Defining the ModelTrainingPipeline class
class ModelTrainingPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        try:
            # Instantiating the ConfigurationManager class
            config_manager = ConfigurationManager()
            # Getting the model training configuration
            model_training_config = config_manager.get_model_training_config()
            # Instantiating the ModelTraining class
            model_training = ModelTraining(config=model_training_config)
            # Training the model
            model_training.train_model()

        except Exception as e:
            logger.exception(e)
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>> Starting {STAGE_NAME} <<<<<")
        ModelTrainingPipeline.main()
        logger.info(f">>>>> Completed {STAGE_NAME} <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
