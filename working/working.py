import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([0-9]+:?(?:[0-9]+)?) ([AP]M) to ([0-9]+:?(?:[0-9]+)?) ([AP]M)", s, re.IGNORECASE):
        converted_start = retrieve(matches.group(1), matches.group(2))
        converted_end = retrieve(matches.group(3), matches.group(4))
        return f"{converted_start} to {converted_end}"
    else:
        raise ValueError


def retrieve(time, apm):
    h = int(time.split(":")[0])
    m = 0
    if ":" in time:
        m = int(time.split(":")[1])

    if h > 12 or m > 59:
        raise ValueError
    else:
        if apm == "PM":
            if h != 12:
                h = h + 12
        else:
            if h == 12:
                h = h - 12
        return f"{h:02}:{m:02}"

if __name__ == "__main__":
    main()