import sys, csv
from tabulate import tabulate

arg_count = len(sys.argv)
table = []

if arg_count == 1:
    sys.exit("Too few command-line arguments")
elif arg_count > 2:
    sys.exit("Too many command-line arguments")
else:
    filename = sys.argv[1]
    if ".csv" in filename:
        try:
            with open(filename, "r") as file:
                readfile = csv.reader(file)
                for row in readfile:
                    table.append(row)
                print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")