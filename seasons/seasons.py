from datetime import date
import inflect, sys, operator

p = inflect.engine()

def convert(dob):
    try:
        day_diff = operator.sub(date.today(), date.fromisoformat(dob)).days
        min_diff = day_diff * 24 * 60
        return min_diff
    except ValueError:
        sys.exit("Invalid date")

def main():
    user_dob = input("Date of Birth: ")
    min_diff_str = p.number_to_words(convert(user_dob), andword="").capitalize()
    print(f"{min_diff_str} minutes")

if __name__ == "__main__":
    main()