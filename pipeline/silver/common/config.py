from pathlib import Path

# Project Paths

PROJECT_ROOT = Path(__file__).resolve().parents[3]

BRONZE_PATH = PROJECT_ROOT / "lakehouse" / "bronze"
SILVER_PATH = PROJECT_ROOT / "lakehouse" / "silver"

# Business Domains

PROCUREMENT = "procurement"
SALES = "sales"
INVENTORY = "inventory"
PRODUCTION = "production"
FINANCE = "finance"
LOGISTICS = "logistics"

# Write Configuration

WRITE_MODE = "overwrite"
COMPRESSION = "snappy"

# Silver Metadata

REJECTS_FOLDER = "rejects"
AUDIT_FOLDER = "audit"
