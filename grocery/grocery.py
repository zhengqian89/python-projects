grocery_input = {}

while True:
    try:
        user = input("").upper()
        if user in grocery_input:
            grocery_input[user] += 1
        else:
            grocery_input[user] = 1
    except EOFError:
        grocery_keys = list(grocery_input.keys())
        grocery_keys.sort()
        for i in grocery_keys:
            print(f"{grocery_input[i]} {i}")
        break