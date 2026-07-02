import csv
import random

from config import PROCUREMENT_DIR
from config import NUM_SUPPLIERS

from master_data import COMPANY_PREFIXES
from master_data import COMPANY_SUFFIXES
from master_data import COMPANY_ENDINGS
from master_data import LOCATIONS
from master_data import SUPPLIER_TYPES

from utils import chance
from utils import generate_code


def generate_suppliers():

    output_file = PROCUREMENT_DIR / "suppliers.csv"

    used_names = set()

    with open(output_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "supplier_id",
            "supplier_code",
            "supplier_name",
            "city",
            "state",
            "supplier_type",
            "status"
        ])

        supplier_id = 1

        while supplier_id <= NUM_SUPPLIERS:

            supplier_name = (
                f"{random.choice(COMPANY_PREFIXES)} "
                f"{random.choice(COMPANY_SUFFIXES)} "
                f"{random.choice(COMPANY_ENDINGS)}"
            ).strip()

            if supplier_name in used_names:
                continue

            used_names.add(supplier_name)

            state = random.choice(list(LOCATIONS.keys()))
            city = random.choice(LOCATIONS[state])

            supplier_type = random.choices(
                SUPPLIER_TYPES,
                weights=[85, 15],
                k=1
            )[0]

            status = "Active" if chance(90) else "Inactive"

            writer.writerow([

                supplier_id,
                generate_code("SUP", supplier_id),
                supplier_name,
                city,
                state,
                supplier_type,
                status

            ])

            supplier_id += 1

    print(f"Generated {NUM_SUPPLIERS} suppliers.")


if __name__ == "__main__":

    generate_suppliers()
