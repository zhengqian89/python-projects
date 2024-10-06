import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if hour := re.search("([0-9]+:?[0-9]+)? ([AP]M) to ([0-9]+:?[0-9]+)? ([AP]M)", s):
        start = hour.group(1)
        start_apm = hour.group(2)
        end = hour.group(3)
        end_apm = hour.group(4)
        return f"{splitter(start, start_apm)} to {splitter(end, end_apm)}"

def splitter(time, apm):
    hour = 0
    min = 0
    if ":" in time:
        splitted = time.split(":")
        hour = int(splitted[0])
        min = int(splitted[1])
    else:
        hour = int(time)

    if hour >= 13 or min >= 60:
        raise ValueError
    else:
        if apm == "PM":
            hour = hour + 12

        return f"{hour:02}:{min:02}"

if __name__ == "__main__":
    main()