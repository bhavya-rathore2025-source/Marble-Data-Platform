from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    DateType,
    DecimalType
)

# Suppliers

SUPPLIER_SCHEMA = StructType([
    StructField("supplier_id", IntegerType(), False),
    StructField("supplier_code", StringType(), False),
    StructField("supplier_name", StringType(), False),
    StructField("city", StringType(), False),
    StructField("state", StringType(), False),
    StructField("supplier_type", StringType(), False),
    StructField("status", StringType(), False),
])

# Materials

MATERIAL_SCHEMA = StructType([
    StructField("material_id", IntegerType(), False),
    StructField("material_code", StringType(), False),
    StructField("material_name", StringType(), False),
    StructField("material_category", StringType(), False),
    StructField("unit_of_measure", StringType(), False),
    StructField("status", StringType(), False),
])

# Goods Receipts

GOODS_RECEIPT_SCHEMA = StructType([
    StructField("grn_id", IntegerType(), False),
    StructField("po_id", IntegerType(), False),
    StructField("warehouse_id", IntegerType(), False),
    StructField("receipt_date", DateType(), False),
])

# Goods Receipt Lines

GOODS_RECEIPT_LINE_SCHEMA = StructType([
    StructField("grn_line_id", IntegerType(), False),
    StructField("grn_id", IntegerType(), False),
    StructField("po_line_id", IntegerType(), False),
    StructField("quantity_received", DecimalType(10, 2), False),
])
