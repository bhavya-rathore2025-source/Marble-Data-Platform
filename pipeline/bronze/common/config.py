from pathlib import Path

# Project Paths

PROJECT_ROOT = Path(__file__).resolve().parents[3]

SOURCE_DATA_PATH = PROJECT_ROOT / "source_data"
LAKEHOUSE_PATH = PROJECT_ROOT / "lakehouse"

BRONZE_PATH = LAKEHOUSE_PATH / "bronze"

# File Format

FILE_FORMAT = "parquet"

CSV = "csv"
JSON = "json"
API = "api"

COMPRESSION = "snappy"

# Write Configuration

WRITE_MODE = "overwrite"
