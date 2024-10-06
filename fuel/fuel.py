while (True):
    fraction = input("Fraction: ")
    try:
        numerator = int(fraction.partition("/")[0])
        denominator = int(fraction.partition("/")[2])
        result = round(numerator/denominator * 100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if 0 <= result <= 1:
            print("E")
            break
        if 1 < result < 99:
            print(f"{result}%")
            break
        if 99 <= result <= 100:
            print("F")
            break