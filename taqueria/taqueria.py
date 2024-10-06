menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while (True):
    try:
        item=input("Item: ").title()
        total = total + menu[item]
        print(f"Total: ${total:.2f}")
        # print(f"Total: {'%.2f' %total}") # This is a method of placeholder, which also works
    except EOFError:
        print("")
        break
    except KeyError:
        pass

# try:
#     while True:
#         item=input("Item: ").title()
#         if item in menu:
#             total = total + menu[item]
#             print(f"Total: {total:.2f}")
#         else:
#             continue
# except EOFError:
#     print("")