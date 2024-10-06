import re

def main():
    print(count(input("Text: ")))


def count(s):
    word = r"\bum\b"
    matches = re.findall(word, s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()