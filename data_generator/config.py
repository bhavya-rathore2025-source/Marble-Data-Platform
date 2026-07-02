from pathlib import Path

# -----------------------------------
# Project Paths
# -----------------------------------

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

# -----------------------------------
# Business Calendar
# -----------------------------------

START_DATE = "2024-01-01"
END_DATE = "2026-12-31"

# -----------------------------------
# Data Volume
# -----------------------------------

NUM_SUPPLIERS = 500

NUM_PURCHASE_ORDERS = 100000

MIN_PO_LINES = 2
MAX_PO_LINES = 8

MIN_GR_LINES = 1
MAX_GR_LINES = 6

# -----------------------------------
# Random Seed
# -----------------------------------

RANDOM_SEED = 42
