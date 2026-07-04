from procurement.generate_suppliers import generate_suppliers
from procurement.generate_materials import generate_materials
from procurement.generate_purchase_orders import generate_purchase_orders


def main():

    print("Generating procurement data...\n")

    generate_suppliers()
    generate_materials()
    generate_purchase_orders()

    print("\nDone.")


if __name__ == "__main__":
    main()
