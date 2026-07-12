from pyspark.sql import SparkSession
from pyspark.sql.types import StructType


def read_csv(
    spark: SparkSession,
    file_path: str,
    schema: StructType,
):
    """
    Read a CSV file using a predefined schema.
    """
    return (
        spark.read
        .option("header", True)
        .schema(schema)
        .csv(file_path)
    )


def read_json(
    spark: SparkSession,
    file_path: str,
    schema: StructType,
):
    """
    Read a JSON file using a predefined schema.
    """
    return (
        spark.read
        .schema(schema)
        .json(file_path)
    )
