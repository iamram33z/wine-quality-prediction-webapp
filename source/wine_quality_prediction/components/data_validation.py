"""
This module contains the DataValidation class which is responsible for validating the data
"""

# Importing Required Libraries
import pandas as pd
from wine_quality_prediction import logger
from wine_quality_prediction.entity.config_entity import DataValidationConfig


# Defining the DataValidation class
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            wine_data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(wine_data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write(f"Validation Status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write(f"Validation Status: {validation_status}")
            return validation_status

        except Exception as e:
            logger.exception(e)
            raise e
