import json
import random

from config import (
    NUM_PURCHASE_ORDERS,
    PURCHASE_ORDERS_FILE,
    START_DATE,
    END_DATE
)
from helpers import load_active_suppliers

from master_data import (
    PAYMENT_TERMS,
    PO_STATUS,
    PO_STATUS_WEIGHTS
)

from utils import (
    random_date,
    future_date,
    generate_code,
    weighted_choice
)


def generate_purchase_orders():

    purchase_orders = []
    active_suppliers = load_active_suppliers().to_dict("records")

    for po_id in range(1, NUM_PURCHASE_ORDERS + 1):

        supplier = random.choice(active_suppliers)

        order_date = random_date(
            START_DATE,
            END_DATE
        )
        purchase_order = {

            "po_id": po_id,

            "po_number": generate_code("PO", po_id, 8),

            "supplier_id": int(supplier["supplier_id"]),

            "order_date": order_date,

            "expected_delivery_date": future_date(
                order_date,
                3,
                30
            ),

            "currency": (
                "INR"
                if supplier["supplier_type"] == "Domestic"
                else "USD"
            ),

            "payment_term": random.choice(PAYMENT_TERMS),

            "status": weighted_choice(
                PO_STATUS,
                PO_STATUS_WEIGHTS
            )

        }

        purchase_orders.append(purchase_order)

    with open(PURCHASE_ORDERS_FILE, "w", encoding="utf-8") as file:

        json.dump(
            purchase_orders,
            file,
            indent=4
        )

    print(f"Generated {len(purchase_orders):,} purchase orders.")
    print(f"Saved to: {PURCHASE_ORDERS_FILE}")


if __name__ == "__main__":
    generate_purchase_orders()
