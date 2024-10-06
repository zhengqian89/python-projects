answer = str(input("Number: ")).strip()

if answer == "42" or answer.lower() == "forty-two" or answer.lower() == "forty two":
    print("Yes")
else:
    print("No")