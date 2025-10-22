# lines.py
# CS50 Problem Set 6: Lines

import sys

def main():
    # make sure a filename was provided
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]

    # file must be a Python file
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename) as file:
            count = 0
            for line in file:
                # strip whitespace
                stripped = line.strip()
                # ignore blank lines and comments
                if stripped == "" or stripped.startswith("#"):
                    continue
                count += 1
            print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
