def main():
    while True:
        fraction = input("Fraction: ")
        try:
            frac = convert(fraction)
            print(gauge(frac))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    try:
        numerator = int(fraction.split("/")[0])
        denominator = int(fraction.split("/")[1])
        if numerator > denominator and denominator != 0:
            raise ValueError
        else:
            return int(round(numerator/denominator * 100))
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError

    # str_numerator = fraction.partition("/")[0]
    # str_denominator = fraction.partition("/")[2]
    # if str_numerator.isalpha() or str_denominator.isalpha():
    #     raise ValueError
    # else:
    #     numerator = int(str_numerator)
    #     denominator = int(str_denominator)
    #     if numerator > denominator and denominator != 0:
    #         raise ValueError
    #     elif denominator == 0:
    #         raise ZeroDivisionError
    #     else:
    #         return numerator/denominator * 100

def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    if 1 < percentage < 99:
        return f"{percentage}%"
    if 99 <= percentage <= 100:
        return "F"

if __name__ == "__main__":
    main()