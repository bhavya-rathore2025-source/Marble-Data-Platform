import json
from config import PURCHASE_ORDERS_FILE
import pandas as pd
from functools import lru_cache
from config import SUPPLIERS_FILE, MATERIALS_FILE
from config import PURCHASE_ORDER_LINES_FILE


@lru_cache(maxsize=None)
def load_suppliers():
    """
    Load all suppliers.
    """
    return pd.read_csv(SUPPLIERS_FILE)


def load_active_suppliers():
    """
    Load only active suppliers.
    """
    suppliers = load_suppliers()
    return suppliers[suppliers["status"] == "Active"].reset_index(drop=True)


@lru_cache(maxsize=None)
def load_materials():
    """
    Load all materials.
    """
    return pd.read_csv(MATERIALS_FILE)


def load_purchase_orders():

    with open(
        PURCHASE_ORDERS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def load_purchase_order_lines():

    with open(
        PURCHASE_ORDER_LINES_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)
