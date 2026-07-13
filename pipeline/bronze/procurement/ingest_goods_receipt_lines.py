from pipeline.bronze.common.config import SOURCE_DATA_PATH, JSON
from pipeline.bronze.common.ingestion import ingest_table
from pipeline.bronze.common.schemas import GOODS_RECEIPT_LINE_SCHEMA


def ingest_goods_receipt_lines(spark):

    ingest_table(
        spark=spark,
        source_path=SOURCE_DATA_PATH / "procurement" / "goods_receipt_lines.json",
        table_name="goods_receipt_lines",
        source_type=JSON,
        schema=GOODS_RECEIPT_LINE_SCHEMA,
        domain="procurement",
    )
