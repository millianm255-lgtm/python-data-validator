import csv


def validate_csv(file_path):
    valid_rows = 0
    invalid_rows = 0

    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if row.get("name") and row.get("email"):
                valid_rows += 1
            else:
                invalid_rows += 1

    return {
        "valid_rows": valid_rows,
        "invalid_rows": invalid_rows
    }


if __name__ == "__main__":
    result = validate_csv("sample_data.csv")
    print(result)
