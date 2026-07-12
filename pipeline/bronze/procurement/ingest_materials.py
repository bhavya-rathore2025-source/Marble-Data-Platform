from pipeline.bronze.common.config import SOURCE_DATA_PATH, CSV
from pipeline.bronze.common.ingestion import ingest_table
from pipeline.bronze.common.schemas import MATERIAL_SCHEMA


def ingest_materials(spark):

    ingest_table(
        spark=spark,
        source_path=SOURCE_DATA_PATH / "procurement" / "materials.csv",
        table_name="materials",
        source_type=CSV,
        schema=MATERIAL_SCHEMA,
    )
