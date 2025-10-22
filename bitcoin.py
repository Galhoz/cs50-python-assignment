# bitcoin.py
# CS50 Problem Set 4: Bitcoin

import sys
import json
import urllib.request

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        with urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json") as response:
            data = json.load(response)
            rate = float(data["bpi"]["USD"]["rate"].replace(",", ""))
            amount = bitcoins * rate
            print(f"${amount:,.4f}")
    except urllib.error.URLError:
        sys.exit("Error fetching Bitcoin price")

if __name__ == "__main__":
    main()
