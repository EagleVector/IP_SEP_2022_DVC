from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    raw_data_URL: str
    tar_filepath: Path
    untar_filepath: Path
    prepared_datapath: Path