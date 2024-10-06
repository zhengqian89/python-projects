import random


def main():
    user_level = get_level()
    correct = 0
    counter = 3
    left_dig = 0
    right_dig = 0
    for i in range(10):
        left_dig = int(generate_integer(user_level))
        right_dig = int(generate_integer(user_level))
        correct_ans = left_dig + right_dig
        for j in range(3):
            try:
                answer = int(input("{} + {} = ".format(left_dig, right_dig)))
                if answer == correct_ans:
                    correct += 1
                    counter = 3
                    break
                else:
                    print("EEE")
                    counter = counter - 1
                    if counter == 0:
                        print(left_dig, "+", right_dig, "=", correct_ans)
            except ValueError:
                print("EEE")
    print("Score: ", correct)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        one_dig = random.randint(0, 9)
        return one_dig
    elif level == 2:
        two_dig = random.randint(10, 99)
        return two_dig
    elif level == 3:
        three_dig = random.randint(100, 999)
        return three_dig
    else:
        raise ValueError


if __name__ == "__main__":
    main()