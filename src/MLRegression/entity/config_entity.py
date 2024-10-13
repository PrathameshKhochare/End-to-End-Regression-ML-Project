from dataclasses import dataclass
from pathlib import Path

# Data Ingection
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

# Data validation
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

# Data transformation
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    

# Model Training
# @dataclass(frozen=True)
# class ModelTrainerConfig:
#     root_dir: Path
#     train_data_path: Path
#     test_data_path: Path
#     model_name: str
#     alpha: float
#     l1_ratio: float
#     target_column: str

# Model training using RF
@dataclass(frozen=True)
class RandomForestModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    max_depth: int
    random_state: int
    n_estimators: int
    min_samples_split: int
    target_column: str

# Model Evaluation using RF
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    #mlflow_uri: str