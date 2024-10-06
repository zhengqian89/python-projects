def main():
    mealtime = input("What time is it? ")
    converted = convert(mealtime)
    if 7 <= converted <= 8:
        print("breakfast time")
    if 12 <= converted <= 13:
        print("lunch time")
    if 18 <= converted <= 19:
        print("dinner time")

def convert(time):
    x, y = time.split(":")
    final = int(x) + (int(y)/60)
    return final

if __name__ == "__main__":
    main()