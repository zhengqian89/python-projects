import sys, requests

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            amount = float(sys.argv[1])
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
            priceperunit = float(response["bpi"]["USD"]["rate_float"])
            value = amount * priceperunit
            print(f"${value:,.4f}")
        except ValueError:
            sys.exit("Command-line argument is not a number")

except requests.RequestException:
    pass