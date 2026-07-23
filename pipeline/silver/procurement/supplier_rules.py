from pipeline.silver.common.contracts import (
    VALID_SUPPLIER_STATUS,
    VALID_SUPPLIER_TYPES,
)

from pipeline.silver.common.reject_codes import (
    INVALID_STATUS,
    INVALID_TYPE,
)

from pipeline.silver.common.validators import validate_condition

from pyspark.sql.functions import col


def validate_supplier_status(df):
    """
    Validate supplier status.
    """

    return validate_condition(
        df=df,
        condition=col("status").isin(*VALID_SUPPLIER_STATUS),
        reject_reason=INVALID_STATUS,
    )


def validate_supplier_type(df):
    """
    Validate supplier type.
    """

    return validate_condition(
        df=df,
        condition=col("supplier_type").isin(*VALID_SUPPLIER_TYPES),
        reject_reason=INVALID_TYPE,
    )