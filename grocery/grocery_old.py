grocery_final = {}
grocery_temp = {}
counter = 0

while True:
    try:
        fruit = input("").upper()
        if fruit in grocery_final:
            grocery_final[fruit] += 1
        else:
            counter += 1
            loop_breaker = 0
            if counter >= 2:
                for x in list(grocery_final):
                    if loop_breaker == 0:
                        if ord(fruit[0]) < ord(x[0]):
                            grocery_temp[fruit] = 1
                            grocery_temp[x] = grocery_final[x]
                            print(grocery_temp)
                        else:
                            grocery_temp[x] = grocery_final[x]
                            grocery_temp[fruit] = 1
                            print(grocery_temp)
                    else:
                        grocery_temp[x] = grocery_final[x]
                    loop_breaker += 1
                grocery_final = grocery_temp
                    # if ord(fruit[0]) < ord(x[0]):
                    #     if loop_breaker == 0:
                    #         grocery_temp[fruit] = 1
                    #         grocery_temp[x] = grocery_final[x]
                    #     else:
                    #         grocery_temp[x] = grocery_final[x]
                    #     grocery_sorted = grocery_temp
                    # else:
                    #     if loop_breaker == 0:
                    #         grocery_temp[x] = grocery_final[x]
                    #         grocery_temp[fruit] = 1
                    #     else:
                    #         grocery_temp[x] = grocery_final[x]
                    # loop_breaker += 1
            else:
                grocery_final[fruit] = 1
    except EOFError:
        print(grocery_temp)
        break
    except KeyError:
        pass
    except IndexError:
        pass