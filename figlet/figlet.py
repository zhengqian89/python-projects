import sys
import random

# Initiate the use of Figlet module
from pyfiglet import Figlet
figlet = Figlet()

# To obtain a list of available fonts
fontlist = figlet.getFonts()

if len(sys.argv) == 2 or len(sys.argv) > 3:
    sys.exit("Invalid usage")

if len(sys.argv) == 1:
    user_text = input("Input: ")
    sel_font = random.choice(fontlist)

    # Setting font
    figlet.setFont(font=sel_font)

    # Printing input in randomly selected font
    print("Output:\n" + figlet.renderText(user_text))

else:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        user_font = sys.argv[2]
        if user_font in fontlist:
            user_text = input("Input: ")
            figlet.setFont(font=user_font)
            print("Output:\n" + figlet.renderText(user_text))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")