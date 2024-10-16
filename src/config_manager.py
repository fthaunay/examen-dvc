from src.config import CONFIG_FILE_PATH, SCHEMA_FILE_PATH, PARAMS_FILE_PATH
from src.common_utils import read_yaml, create_directories
from src.entity import (DataIngestionConfig, 
                        DataPreparationConfig, 
                        DataTransformationConfig, 
                        GridSearchConfig,
                        ModelTrainerConfig, 
                        ModelEvaluationConfig)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
            schema_filepath=SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
     
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                source_url=config.source_URL,
                local_data_file=config.local_data_file,
          )

        return data_ingestion_config

    def get_data_preparation_config(self) -> DataPreparationConfig:
        config = self.config.data_preparation

        create_directories([config.root_dir])

        data_preparation_config = DataPreparationConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
                target=config.target,
                test_size=config.test_size
          )

        return data_preparation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
          )

        return data_transformation_config

    def get_gridsearch_config(self) -> GridSearchConfig:
        config = self.config.gridsearch
          
        create_directories([config.root_dir])

        gridsearch_config = GridSearchConfig(
                root_dir=config.root_dir,
                X_train_path=config.X_train_path,
                y_train_path=config.y_train_path,
                X_test_path=config.X_test_path,
                y_test_path=config.y_test_path,
                params_file=config.params_file
          )

        return gridsearch_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
          
        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
                root_dir=config.root_dir,
                X_train_path=config.X_train_path,
                y_train_path=config.y_train_path,
                X_test_path=config.X_test_path,
                y_test_path=config.y_test_path,
                model_name=config.model_name,
                params_file=config.params_file
          )

        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet

        create_directories([config.root_dir])
          
        model_evaluation_config = ModelEvaluationConfig(
                root_dir=config.root_dir,
                X_test_path=config.X_test_path,
                y_test_path=config.y_test_path,
                model_path=config.model_path,
                metric_file_name=config.metric_file_name,
                all_params=params,
                mlflow_uri="https://dagshub.com/florian.thaunay/examen-dvc",
          )

        return model_evaluation_config