from pyspark.sql import DataFrame
from pathlib import Path


from .config import WRITE_MODE, COMPRESSION
from .paths import (
    silver_table_path,
    reject_table_path,
    audit_table_path,
)


def _write(
    df: DataFrame,
    path: Path,
) -> None:
    """
    Internal helper for writing DataFrames.
    """

    (
        df.write
        .mode(WRITE_MODE)
        .option("compression", COMPRESSION)
        .parquet(str(path))
    )


def write_silver(
    df: DataFrame,
    domain: str,
    table_name: str,
) -> None:
    """
    Write validated records to the Silver layer.
    """

    _write(
        df,
        silver_table_path(domain, table_name),
    )


def write_rejects(
    df: DataFrame,
    table_name: str,
) -> None:
    """
    Write rejected records.
    """

    _write(
        df,
        reject_table_path(table_name),
    )


def write_audit(
    df: DataFrame,
) -> None:
    """
    Write pipeline audit records.
    """

    _write(
        df,
        audit_table_path(),
    )
