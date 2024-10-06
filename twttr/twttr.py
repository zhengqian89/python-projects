user = input("Input: ")
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
to_be_printed = user

for char in user:
    if char in vowel:
        to_be_printed = to_be_printed.replace(char, "")

print(f"Output: {to_be_printed}")