import sys

arg_count = len(sys.argv)

if arg_count == 1:
    sys.exit("Too few command-line arguments")
elif arg_count > 2:
    sys.exit("Too many command-line arguments")
else:
    filename = sys.argv[1]
    if ".py" in filename:
        try:
            with open(filename, "r") as file:
                loc_count = 0
                for row in file:
                    if len(row.lstrip()) > 1 and not row.lstrip().startswith("#"):
                        loc_count += 1
                print(loc_count)
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")