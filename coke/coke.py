amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    inserted = int(input("Insert Coin: "))
    if inserted not in [25, 10, 5]:
        continue
    amount_due -= inserted
    if amount_due > 0:
        continue
    else:
        print(f"Change Owed: {-amount_due}")