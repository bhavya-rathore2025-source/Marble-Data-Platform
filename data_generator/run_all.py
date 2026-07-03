from procurement.generate_suppliers import generate_suppliers


def main():

    print("Generating procurement data...\n")

    generate_suppliers()

    print("\nDone.")


if __name__ == "__main__":
    main()
