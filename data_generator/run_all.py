from procurement.generate_suppliers import generate_suppliers
from procurement.generate_materials import generate_materials


def main():

    print("Generating procurement data...\n")

    generate_suppliers()
    generate_materials()

    print("\nDone.")


if __name__ == "__main__":
    main()
