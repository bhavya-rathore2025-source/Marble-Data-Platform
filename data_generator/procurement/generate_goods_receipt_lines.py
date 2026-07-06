import json

from collections import defaultdict

from config import GOODS_RECEIPT_LINES_FILE

from helpers import (
    load_goods_receipts,
    load_purchase_order_lines
)


def generate_goods_receipt_lines():

    goods_receipts = load_goods_receipts()

    purchase_order_lines = load_purchase_order_lines()

    po_lines_by_po = defaultdict(list)

    for po_line in purchase_order_lines:

        po_lines_by_po[
            po_line["po_id"]
        ].append(po_line)

    goods_receipt_lines = []

    grn_line_id = 1

    for goods_receipt in goods_receipts:

        po_lines = po_lines_by_po[
            goods_receipt["po_id"]
        ]

        for po_line in po_lines:

            goods_receipt_lines.append({

                "grn_line_id": grn_line_id,

                "grn_id": goods_receipt["grn_id"],

                "po_line_id": po_line["po_line_id"],

                "quantity_received": po_line["ordered_quantity"]

            })

            grn_line_id += 1

    with open(
        GOODS_RECEIPT_LINES_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            goods_receipt_lines,
            file,
            indent=4
        )

    print(
        f"Generated {len(goods_receipt_lines):,} goods receipt lines."
    )

    print(
        f"Saved to: {GOODS_RECEIPT_LINES_FILE}"
    )


if __name__ == "__main__":
    generate_goods_receipt_lines()
