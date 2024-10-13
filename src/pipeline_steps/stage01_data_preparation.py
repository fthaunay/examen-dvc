import sys
from pathlib import Path

# Add parent directory to path
parent_folder = str(Path(__file__).parent.parent.parent)
sys.path.append(parent_folder)
print(parent_folder)

from src.config_manager import ConfigurationManager
from src.data_module_def.data_preparation import DataPreparation
from custom_logger import logger

STAGE_NAME = "Data Preparation stage"

# Le jeu de données contient 1817 entrées, 
# toutes les colonnes sont de type float64 
# et il n'y a pas de doublons ni de valeurs manquantes


class DataPreparationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_preparation_config = config.get_data_preparation_config()
        data_preparation = DataPreparation(config=data_preparation_config)

        data_preparation.train_test_splitting()
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataPreparationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e