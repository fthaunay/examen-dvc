import sys
from pathlib import Path

# Add parent directory to path
parent_folder = str(Path(__file__).parent.parent.parent)
sys.path.append(parent_folder)

from src.config_manager import ConfigurationManager
from src.models_module_def.model_gridsearch import ModelGridSearch
from custom_logger  import logger

STAGE_NAME = "Data Transformation stage"


class GridSearchPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        gridsearch_config = config.get_gridsearch_config()
        gridsearch = ModelGridSearch(config=gridsearch_config)

        gridsearch.define()


if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = GridSearchPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e