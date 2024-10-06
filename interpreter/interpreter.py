expression = input("Expression: ")

x, y, z = expression.split(" ")

def main():
    first = int(x)
    second = int(z)
    result = 0
    if y == "/":
        if second == 0:
            return False
        else:
            result = first / second
            print (result)
    if y == "*":
        result = first * second
        print (float(result))
    if y == "-":
        result = first - second
        print (float(result))
    if y == "+":
        result = first + second
        print (float(result))
    else:
        return False

main()