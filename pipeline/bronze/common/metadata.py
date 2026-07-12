from pyspark.sql import DataFrame
from pyspark.sql.functions import current_timestamp, lit


def add_metadata(
    df: DataFrame,
    source_system: str
) -> DataFrame:
    """
    Add Bronze metadata columns.
    """

    return (
        df.withColumn("ingestion_timestamp", current_timestamp())
          .withColumn("source_system", lit(source_system))
    )
