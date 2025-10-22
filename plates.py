# plates.py
# CS50 Problem Set 2: Vanity Plates

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # 2–6 characters
    if not (2 <= len(s) <= 6):
        return False

    # must start with at least two letters
    if not s[:2].isalpha():
        return False

    number_started = False
    for i, c in enumerate(s):
        if c.isdigit():
            if not number_started:
                # first number cannot be 0
                if c == "0":
                    return False
                number_started = True
        else:
            # once numbers start, no more letters allowed
            if number_started:
                return False

        # only letters and numbers allowed
        if not c.isalnum():
            return False

    return True

if __name__ == "__main__":
    main()
