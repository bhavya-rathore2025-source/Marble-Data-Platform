from pyspark.sql import SparkSession

from pipeline.bronze.procurement.ingest_suppliers import ingest_suppliers
from pipeline.bronze.procurement.ingest_materials import ingest_materials
from pipeline.bronze.procurement.ingest_goods_receipts import ingest_goods_receipts
from pipeline.bronze.procurement.ingest_goods_receipt_lines import ingest_goods_receipt_lines


def main():

    spark = (
        SparkSession.builder
        .appName("Bronze Procurement Pipeline")
        .getOrCreate()
    )

    ingest_suppliers(spark)
    ingest_materials(spark)
    ingest_goods_receipts(spark)
    ingest_goods_receipt_lines(spark)

    spark.stop()


if __name__ == "__main__":
    main()
