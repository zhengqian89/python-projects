month = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    try:
        user = input("Date: ")
        slash = user.find("/")
        comma = user.find(",")
        if slash != -1 and comma == -1:
            slash_split = user.split("/")
            s_year = int(slash_split[2])
            s_month = int(slash_split[0])
            s_day = int(slash_split[1])
            if s_day > 31 or s_month > 12:
                pass
            else:
                print(f"{s_year}-{s_month:02}-{s_day:02}")
                break
        elif slash == -1 and comma != -1:
            comma_split = user.split()
            c_year = int(comma_split[2])
            c_day = int(comma_split[1].split(",")[0])
            if comma_split[0] in month and c_day <= 31:
                c_month = int(month[comma_split[0]])
                print(f"{c_year}-{c_month:02}-{c_day:02}")
                break
            else:
                pass
        else:
            pass
    except ValueError:
        pass