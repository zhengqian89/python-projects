import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Retrive src
    if src := re.search(r'<iframe[^>]*\s+src="([^"]+)"', s):
        if matches := re.search(r"https?://(?:www\.)?youtube\.com/embed/(\w+)", src.group(1)):
            return f"https://youtu.be/{matches.group(1)}"
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    main()

def main():
    print(parse(input("HTML: ")))