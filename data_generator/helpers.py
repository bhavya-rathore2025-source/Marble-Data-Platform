import pandas as pd
from functools import lru_cache
from config import SUPPLIERS_FILE, MATERIALS_FILE


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
