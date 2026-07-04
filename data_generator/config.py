from pathlib import Path

# Project Paths

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent

# Source Data
SOURCE_DATA_DIR = PROJECT_ROOT / "source_data"

PROCUREMENT_DIR = SOURCE_DATA_DIR / "procurement"
INVENTORY_DIR = SOURCE_DATA_DIR / "inventory"
PRODUCTION_DIR = SOURCE_DATA_DIR / "production"
SALES_DIR = SOURCE_DATA_DIR / "sales"
FINANCE_DIR = SOURCE_DATA_DIR / "finance"
LOGISTICS_DIR = SOURCE_DATA_DIR / "logistics"

# API Data
API_DATA_DIR = PROJECT_ROOT / "api" / "data"

# Source Files

SUPPLIERS_FILE = PROCUREMENT_DIR / "suppliers.csv"
MATERIALS_FILE = PROCUREMENT_DIR / "materials.csv"

PURCHASE_ORDERS_FILE = API_DATA_DIR / "purchase_orders.json"
PURCHASE_ORDER_LINES_FILE = API_DATA_DIR / "purchase_order_lines.json"

GOODS_RECEIPTS_FILE = PROCUREMENT_DIR / "goods_receipts.json"
GOODS_RECEIPT_LINES_FILE = PROCUREMENT_DIR / "goods_receipt_lines.json"

# Create Runtime Directories

for directory in [

    PROCUREMENT_DIR,
    INVENTORY_DIR,
    PRODUCTION_DIR,
    SALES_DIR,
    FINANCE_DIR,
    LOGISTICS_DIR,
    API_DATA_DIR

]:

    directory.mkdir(parents=True, exist_ok=True)


START_DATE = "2024-01-01"
END_DATE = "2026-12-31"

NUM_SUPPLIERS = 200
NUM_MATERIALS = 500

NUM_PURCHASE_ORDERS = 100_000

MIN_PO_LINES = 2
MAX_PO_LINES = 8

MIN_GR_LINES = 1
MAX_GR_LINES = 6

WAREHOUSE_COUNT = 5

RANDOM_SEED = 42
