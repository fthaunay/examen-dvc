from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path


@dataclass(frozen=True)
class DataPreparationConfig:
    root_dir: Path
    data_path: Path
    target: str
    test_size: float


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    


@dataclass(frozen=True)
class GridSearchConfig:
    root_dir: Path
    X_train_path: Path
    y_train_path: Path
    X_test_path: Path
    y_test_path: Path
    params_file: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    X_train_path: Path
    y_train_path: Path
    X_test_path: Path
    y_test_path: Path
    model_name: str
    params_file: Path


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    X_test_path: Path
    y_test_path: Path
    model_path: Path
    metric_file_name: Path
    all_params: dict
    metric_file_name: Path
    mlflow_uri: str
