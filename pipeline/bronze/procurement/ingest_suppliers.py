from pipeline.bronze.common.config import SOURCE_DATA_PATH, CSV
from pipeline.bronze.common.ingestion import ingest_table
from pipeline.bronze.common.schemas import SUPPLIER_SCHEMA


def ingest_suppliers(spark):

    ingest_table(
        spark=spark,
        source_path=SOURCE_DATA_PATH / "procurement" / "suppliers.csv",
        table_name="suppliers",
        source_type=CSV,
        schema=SUPPLIER_SCHEMA,
        domain="procurement",
    )
