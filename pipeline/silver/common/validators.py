"""
Reusable validation functions for the Silver layer.

Each validator splits an input DataFrame into:

1. Valid records
2. Rejected records

Validators DO NOT:
- write data
- collect metrics
- perform logging
- maintain state

They only validate and return DataFrames.
"""

from pyspark.sql import DataFrame
from pyspark.sql.functions import col, current_timestamp, lit


def validate_condition(
    *,
    df: DataFrame,
    condition,
    reject_reason: str,
) -> tuple[DataFrame, DataFrame]:
    """
    Validate rows using a boolean Spark condition.

    Parameters
    ----------
    df : DataFrame
        Input DataFrame.

    condition :
        Spark SQL boolean expression.

    reject_reason : str
        Standard reject code.

    Returns
    -------
    (valid_df, reject_df)
    """

    valid_df = df.filter(condition)

    reject_df = (
        df.filter(~condition)
        .withColumn("reject_reason", lit(reject_reason))
        .withColumn("rejected_timestamp", current_timestamp())
    )

    return valid_df, reject_df


def validate_foreign_key(
    *,
    child_df: DataFrame,
    parent_df: DataFrame,
    child_key: str,
    parent_key: str,
    reject_reason: str,
) -> tuple[DataFrame, DataFrame]:
    """
    Validate foreign-key relationships.

    Parameters
    ----------
    child_df : DataFrame
        DataFrame containing the foreign key.

    parent_df : DataFrame
        Parent DataFrame containing the primary key.

    child_key : str
        Foreign key column.

    parent_key : str
        Parent primary key column.

    reject_reason : str
        Standard reject code.

    Returns
    -------
    (valid_df, reject_df)
    """

    parent_keys = parent_df.select(parent_key).distinct()

    valid_df = child_df.join(
        parent_keys,
        child_df[child_key] == parent_keys[parent_key],
        "left_semi",
    )

    reject_df = (
        child_df.join(
            parent_keys,
            child_df[child_key] == parent_keys[parent_key],
            "left_anti",
        )
        .withColumn("reject_reason", lit(reject_reason))
        .withColumn("rejected_timestamp", current_timestamp())
    )

    return valid_df, reject_df
