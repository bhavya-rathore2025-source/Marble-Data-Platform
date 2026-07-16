"""
Business Data Contracts

This module defines the allowed business values enforced by the
Silver layer during validation.

These contracts represent enterprise business rules rather than
data generation rules.
"""

# Supplier Contracts

from data_generator.master_data import (
    MATERIAL_CATEGORIES,
    UNITS,
    PAYMENT_TERMS,
    PO_STATUS,
)
VALID_SUPPLIER_STATUS = {
    "Active",
    "Inactive",
}

VALID_SUPPLIER_TYPES = {
    "Domestic",
    "International",
}

# Material Contracts

VALID_MATERIAL_CATEGORIES = set(MATERIAL_CATEGORIES)

VALID_UNITS = set(UNITS)

# Purchase Order Contracts

VALID_PO_STATUS = set(PO_STATUS)

VALID_PAYMENT_TERMS = set(PAYMENT_TERMS)

VALID_CURRENCIES = {
    "INR",
    "USD",
}

# Warehouse Contracts

VALID_WAREHOUSE_IDS = {
    1,
    2,
    3,
    4,
    5,
}
