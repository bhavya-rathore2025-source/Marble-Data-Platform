import json
import random
from datetime import datetime, timedelta

from config import (
    GOODS_RECEIPTS_FILE,
    WAREHOUSE_COUNT
)

from helpers import load_purchase_orders


def generate_goods_receipts():

    purchase_orders = load_purchase_orders()

    goods_receipts = []

    grn_id = 1

    for purchase_order in purchase_orders:

        status = purchase_order["status"]

        generate_grn = False

        if status == "Closed":

            generate_grn = True

        elif status == "Approved":

            generate_grn = random.random() < 0.5

        if not generate_grn:
            continue

        expected_delivery = datetime.strptime(
            purchase_order["expected_delivery_date"],
            "%Y-%m-%d"
        )

        receipt_date = expected_delivery + timedelta(
            days=random.randint(-2, 10)
        )

        goods_receipts.append({

            "grn_id": grn_id,

            "po_id": purchase_order["po_id"],

            "warehouse_id": random.randint(
                1,
                WAREHOUSE_COUNT
            ),

            "receipt_date": receipt_date.strftime("%Y-%m-%d")

        })

        grn_id += 1

    with open(
        GOODS_RECEIPTS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            goods_receipts,
            file,
            indent=4
        )

    print(
        f"Generated {len(goods_receipts):,} goods receipts."
    )

    print(
        f"Saved to: {GOODS_RECEIPTS_FILE}"
    )


if __name__ == "__main__":
    generate_goods_receipts()
