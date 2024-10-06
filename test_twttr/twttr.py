def main():
    user = input("Input: ")
    to_be_printed = shorten(user)
    print(f"Output: {to_be_printed}")

def shorten(word):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in word:
        if char in vowel:
            word = word.replace(char, "")

    return word


if __name__ == "__main__":
    main()