import csv
import random

from config import PROCUREMENT_DIR
from config import NUM_MATERIALS
from master_data import MATERIAL_VARIANTS
from master_data import MATERIALS
from master_data import MATERIAL_STATUS
from master_data import UNITS_OF_MEASURE

from utils import chance
from utils import generate_code


def generate_materials():

    output_file = PROCUREMENT_DIR / "materials.csv"

    used_names = set()

    with open(output_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([

            "material_id",
            "material_code",
            "material_name",
            "material_category",
            "unit_of_measure",
            "status"

        ])

        material_id = 1

        while material_id <= NUM_MATERIALS:

            category = random.choice(list(MATERIALS.keys()))

            base_material = random.choice(MATERIALS[category])

            variant = random.choice(MATERIAL_VARIANTS)

            material_name = f"{base_material} {variant}"

            if material_name in used_names:
                continue

            used_names.add(material_name)

            writer.writerow([

                material_id,
                generate_code("MAT", material_id),
                material_name,
                category,
                random.choice(UNITS_OF_MEASURE),
                "Active" if chance(95) else "Inactive"

            ])

            material_id += 1

    print(f"Generated {NUM_MATERIALS} materials.")


if __name__ == "__main__":

    generate_materials()
