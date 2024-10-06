greeting = (input("Greet me: ").lower()).strip()

first_char = greeting.find('h', 0, 1)
hello = greeting.find('hello')

if first_char == 0:
    if hello == -1:
        print("$20")
    else:
        print("$0")
else:
    print("$100")