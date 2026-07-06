from procurement.generate_suppliers import generate_suppliers
from procurement.generate_materials import generate_materials
from procurement.generate_purchase_orders import generate_purchase_orders
from procurement.generate_purchase_order_lines import generate_purchase_order_lines
from procurement.generate_goods_receipts import generate_goods_receipts


def main():

    print("Generating procurement data...\n")

    # generate_suppliers()
    # generate_materials()
    # generate_purchase_orders()
    # generate_purchase_order_lines()
    generate_goods_receipts()
    print("\nDone.")


if __name__ == "__main__":
    main()
