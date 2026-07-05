import json
import random

from config import (
    PURCHASE_ORDERS_FILE,
    PURCHASE_ORDER_LINES_FILE,
    MIN_PO_LINES,
    MAX_PO_LINES
)

from helpers import (
    load_materials,
    load_purchase_orders
)

from master_data import MATERIAL_PRICE_RANGES


def generate_purchase_order_lines():

    purchase_orders = load_purchase_orders()

    materials = load_materials().to_dict("records")

    purchase_order_lines = []

    po_line_id = 1

    for purchase_order in purchase_orders:

        line_count = random.randint(
            MIN_PO_LINES,
            MAX_PO_LINES
        )

        selected_materials = random.sample(
            materials,
            line_count
        )

        for material in selected_materials:

            min_price, max_price = MATERIAL_PRICE_RANGES[
                material["material_category"]
            ]

            purchase_order_lines.append({

                "po_line_id": po_line_id,

                "po_id": purchase_order["po_id"],

                "material_id": int(material["material_id"]),

                "ordered_quantity": random.randint(10, 500),

                "unit_price": round(
                    random.uniform(
                        min_price,
                        max_price
                    ),
                    2
                )

            })

            po_line_id += 1

    with open(
        PURCHASE_ORDER_LINES_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            purchase_order_lines,
            file,
            indent=4
        )

    print(
        f"Generated {len(purchase_order_lines):,} purchase order lines."
    )

    print(
        f"Saved to: {PURCHASE_ORDER_LINES_FILE}"
    )


if __name__ == "__main__":
    generate_purchase_order_lines()
