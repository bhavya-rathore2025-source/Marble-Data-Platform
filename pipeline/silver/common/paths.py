from pathlib import Path

from .config import (
    BRONZE_PATH,
    SILVER_PATH,
    REJECTS_FOLDER,
    AUDIT_FOLDER,
)


def bronze_table_path(domain: str, table_name: str) -> Path:
    return BRONZE_PATH / domain / table_name


def silver_table_path(domain: str, table_name: str) -> Path:
    return SILVER_PATH / domain / table_name


def reject_table_path(table_name: str) -> Path:
    return SILVER_PATH / REJECTS_FOLDER / table_name


def audit_table_path() -> Path:
    return SILVER_PATH / AUDIT_FOLDER
