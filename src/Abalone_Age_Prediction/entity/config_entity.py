from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionManipulationConfig:
    root_dir: Path
    local_data_file: Path
    source_URL: str
    save_training_file: Path
    target_col: str


@dataclass(frozen=True)
class ModelPreparationTrainingConfig:
    root_dir: Path
    local_data_file: Path
    trained_model_path: Path
    param_n_estim_rfr: int
    param_random_state: int
    param_alpha_lasso: float
    param_alpha_ridge: float
    param_alpha_elastic: float
    param_l1_elastic: float
    param_c_svr: float
    param_target_col: str


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    local_data_file: Path
    trained_model_path: Path
    best_model_path: Path
    param_target_col: str
    elastic_pickle: Path
    lasso_pickle: Path
    lr_pickle: Path
    rfr_pickle: Path
    ridge_pickle: Path
    svr_pickle: Path