import random

while True:
    try:
        level = int(input("Level: "))
        if level >= 1:
            answer = random.randint(1, level)
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess == answer:
                        print("Just right!")
                        break
                    elif guess > answer:
                        print("Too large!")
                    else:
                        print("Too small!")
                except ValueError:
                    pass
            break
        else:
            pass
    except ValueError:
        pass
    except EOFError:
        print("")
        break