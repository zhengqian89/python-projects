import inflect

p = inflect.engine()
namelist = []

while True:
    try:
        user = input("Name: ")
        namelist.append(user)
    except EOFError:
        print(f"\nAdieu, adieu, to {p.join(namelist)}")
        break


# import inflect

# p = inflect.engine()
# namelist = []

# while True:
#     try:
#         user = input("Name: ")
#         namelist.append(user)
#     except EOFError:
#         no_of_name = len(namelist)
#         if no_of_name == 2:
#             print("Adiue, adieu, to ", namelist[0], "and", namelist[1])
#         else:
#             joined_name = p.join(namelist)
#             print("Adiue, adieu, to ", p.join(namelist))
#         break