def main():
    greeting = (input("Greet me: ")).strip()
    output = value(greeting)
    print(f"${output}")

def value(greeting):
    lowered_greeting = greeting.lower()
    first_char = lowered_greeting.find('h', 0, 1)
    hello = lowered_greeting.find('hello')

    if first_char == 0:
        if hello == -1:
            return 20
        else:
            return 0
    else:
        return 100


if __name__ == "__main__":
    main()