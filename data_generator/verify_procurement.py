import json
import pandas as pd

from config import (
    SUPPLIERS_FILE,
    MATERIALS_FILE,
    PURCHASE_ORDERS_FILE,
    PURCHASE_ORDER_LINES_FILE,
    GOODS_RECEIPTS_FILE,
    GOODS_RECEIPT_LINES_FILE
)


def verify_relationship(child_name, child_keys, parent_name, parent_keys):

    invalid = child_keys - parent_keys

    if invalid:
        print(f"❌ {child_name} -> {parent_name}")
        print(f"   Invalid references: {len(invalid)}")
        print(f"   Sample: {list(invalid)[:10]}")
    else:
        print(f"✅ {child_name} -> {parent_name}")


def main():

    print("\nProcurement Relationship Verification\n")

    suppliers = pd.read_csv(SUPPLIERS_FILE)
    materials = pd.read_csv(MATERIALS_FILE)

    with open(PURCHASE_ORDERS_FILE, "r", encoding="utf-8") as file:
        purchase_orders = json.load(file)

    with open(PURCHASE_ORDER_LINES_FILE, "r", encoding="utf-8") as file:
        purchase_order_lines = json.load(file)

    with open(GOODS_RECEIPTS_FILE, "r", encoding="utf-8") as file:
        goods_receipts = json.load(file)

    with open(GOODS_RECEIPT_LINES_FILE, "r", encoding="utf-8") as file:
        goods_receipt_lines = json.load(file)

    supplier_ids = set(suppliers["supplier_id"])
    material_ids = set(materials["material_id"])

    po_ids = {
        po["po_id"]
        for po in purchase_orders
    }

    po_line_ids = {
        line["po_line_id"]
        for line in purchase_order_lines
    }

    grn_ids = {
        grn["grn_id"]
        for grn in goods_receipts
    }

    verify_relationship(
        "Purchase Orders",
        {
            po["supplier_id"]
            for po in purchase_orders
        },
        "Suppliers",
        supplier_ids
    )

    verify_relationship(
        "Purchase Order Lines",
        {
            line["po_id"]
            for line in purchase_order_lines
        },
        "Purchase Orders",
        po_ids
    )

    verify_relationship(
        "Purchase Order Lines",
        {
            line["material_id"]
            for line in purchase_order_lines
        },
        "Materials",
        material_ids
    )

    verify_relationship(
        "Goods Receipts",
        {
            grn["po_id"]
            for grn in goods_receipts
        },
        "Purchase Orders",
        po_ids
    )

    verify_relationship(
        "Goods Receipt Lines",
        {
            line["grn_id"]
            for line in goods_receipt_lines
        },
        "Goods Receipts",
        grn_ids
    )

    verify_relationship(
        "Goods Receipt Lines",
        {
            line["po_line_id"]
            for line in goods_receipt_lines
        },
        "Purchase Order Lines",
        po_line_ids
    )


if __name__ == "__main__":
    main()
