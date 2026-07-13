from pyspark.sql import DataFrame

from .config import BRONZE_PATH, WRITE_MODE, COMPRESSION


def write_bronze(
    df: DataFrame,
    domain: str,
    table_name: str,
) -> None:
    """
    Write a DataFrame to the Bronze layer.
    """

    (
        df.write
        .mode(WRITE_MODE)
        .option("compression", COMPRESSION)
        .parquet(str(BRONZE_PATH / domain / table_name))
    )
