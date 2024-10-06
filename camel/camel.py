camel = input("camelCase: ")
camel_output = camel

for char in camel:
    if char.isupper():
        camel_output = camel_output.replace(char, "_" + char.lower())

print(camel_output)

# word = "stRiNg"
# new_word = word
# for char in word:
#     if char.isupper():
#         new_word = new_word.replace(char, "_" + char.lower())
# print(new_word)
