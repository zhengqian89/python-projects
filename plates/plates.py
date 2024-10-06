def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length(s) and check_punc(s):
        if check_all_alpha(s):
            return True
        else:
            return mid_last_checker(s) and first_zero(s)
    else:
        return False

def first_two(s):
    if s[0:1].isalpha():
        return True
    else:
        return False

def length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def check_punc(s):
    for i in s:
        if i.isalnum() == False:
            return False
    return True

def mid_last_checker(s):
    num_counter = 0
    if s[-1].isnumeric():
        return True
    else:
        for char in s:
            if char.isnumeric():
                num_counter += 1
        if num_counter > 0:
            return False
        else:
            return True

def first_zero(s):
    zero_counter = -1
    for char in s:
        if char.isalpha():
            zero_counter += 1
            if zero_counter + 1 != len(s):
                if s[zero_counter + 1].isalpha():
                    continue
                else:
                    if s[zero_counter + 1] == '0':
                        return False
            else:
                return False
    if zero_counter == -1:
        return False
    else:
        if s[zero_counter + 1] == '0':
            return False
        else:
            return True

def check_all_alpha(s):
    sol = True
    for char in s:
        if char.isnumeric():
            sol = False
    return sol

main()