from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionManipulationConfig:
    root_dir: Path
    local_data_file: Path
    source_URL: str
    save_training_file: Path
    target_col: str