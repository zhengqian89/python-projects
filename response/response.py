import validators

def main():
    print(valid_email(input("What's your email address? ")))

def valid_email(email):
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()