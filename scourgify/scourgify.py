import sys, csv

arg_count = len(sys.argv)

if arg_count == 1:
    sys.exit("Too few command-line arguments")
elif arg_count > 3:
    sys.exit("Too many command-line arguments")
else:
    before = sys.argv[1]
    after = sys.argv[2]
    if ".csv" not in before:
        sys.exit(f"Could not read {before}")
    else:
        try:
            with open(before, "r") as csvfile:
                before_read = csv.DictReader(csvfile)
                with open(after, "w", newline="") as new_file:
                    header = ["first", "last", "house"]
                    writer = csv.DictWriter(new_file, fieldnames=header)
                    writer.writeheader()
                    for row in before_read:
                        name = row["name"].split(",")
                        first = name[1].strip()
                        last = name[0].strip()
                        house = row["house"].strip()
                        writer.writerow({"first": first, "last": last, "house": house})

        except FileNotFoundError:
            sys.exit(f"Could not read {before}")