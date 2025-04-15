import json
import sys

FILE_PATH = "brands.json"


def validate_json():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        sys.exit(1)

    if not isinstance(data, list):
        print("JSON is not a list.")
        sys.exit(1)

    sorted_data = sorted(data, key=lambda x: x.lower())
    if data != sorted_data:
        print("Items are not in case-insensitive alphabetical order.")
        for original, sorted_item in zip(data, sorted_data):
            if original != sorted_item:
                print(f"Mismatch: {original} should be {sorted_item}")
        sys.exit(1)

    print("brands.json is valid and items are in alphabetical order.")


if __name__ == "__main__":
    validate_json()
