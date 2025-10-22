# coke.py
# CS50 Problem Set 2: Coke Machine

def main():
    amount_due = 50
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        if coin in [25, 10, 5]:
            amount_due -= coin
        else:
            print("Invalid coin.")
    print(f"Change Owed: {-amount_due}")

if __name__ == "__main__":
    main()
