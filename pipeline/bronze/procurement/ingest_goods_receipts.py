from pipeline.bronze.common.config import SOURCE_DATA_PATH, JSON
from pipeline.bronze.common.ingestion import ingest_table
from pipeline.bronze.common.schemas import GOODS_RECEIPT_SCHEMA


def ingest_goods_receipts(spark):

    ingest_table(
        spark=spark,
        source_path=SOURCE_DATA_PATH / "procurement" / "goods_receipts.json",
        table_name="goods_receipts",
        source_type=JSON,
        schema=GOODS_RECEIPT_SCHEMA,
    )
