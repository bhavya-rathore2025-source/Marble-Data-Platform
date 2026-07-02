from pathlib import Path

# Project paths

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent

SOURCE_DATA_DIR = PROJECT_ROOT / "source_data"

PROCUREMENT_DIR = SOURCE_DATA_DIR / "procurement"
INVENTORY_DIR = SOURCE_DATA_DIR / "inventory"
PRODUCTION_DIR = SOURCE_DATA_DIR / "production"
SALES_DIR = SOURCE_DATA_DIR / "sales"
FINANCE_DIR = SOURCE_DATA_DIR / "finance"
LOGISTICS_DIR = SOURCE_DATA_DIR / "logistics"

API_DATA_DIR = PROJECT_ROOT / "api" / "data"

# Create directories

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

# Business calendar

START_DATE = "2024-01-01"
END_DATE = "2026-12-31"

# Data volumes

NUM_SUPPLIERS = 200
NUM_MATERIALS = 500

NUM_PURCHASE_ORDERS = 100000

MIN_PO_LINES = 2
MAX_PO_LINES = 8

MIN_GR_LINES = 1
MAX_GR_LINES = 6

# Warehouses

WAREHOUSE_COUNT = 5

# Random seed

RANDOM_SEED = 42
