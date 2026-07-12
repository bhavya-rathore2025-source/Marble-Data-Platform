from pyspark.sql import SparkSession
from pyspark.sql.types import StructType

from .metadata import add_metadata
from .readers import read_csv, read_json
from .writer import write_bronze


def ingest_table(
    spark: SparkSession,
    source_path: str,
    table_name: str,
    source_type: str,
    schema: StructType,
) -> None:
    """
    Generic Bronze ingestion pipeline.
    """

    if source_type == "csv":
        df = read_csv(spark, source_path, schema)

    elif source_type == "json":
        df = read_json(spark, source_path, schema)

    else:
        raise ValueError(f"Unsupported source type: {source_type}")

    df = add_metadata(df, source_type)

    write_bronze(df, table_name)
