import sys, os
from PIL import Image, ImageOps

arg_count = len(sys.argv)

if arg_count == 1:
    sys.exit("Too few command-line arguments")
elif arg_count > 3:
    sys.exit("Too many command-line arguments")
else:
    input = sys.argv[1]
    output = sys.argv[2]
    input_ext = os.path.splitext(input)[1]
    output_ext = os.path.splitext(output)[1]
    accepted = [".jpg", ".jpeg", ".png"]
    if input_ext.find(".") != -1 and output_ext.find(".") != -1:
        if input_ext not in accepted:
            sys.exit("Invalid input")
        elif output_ext not in accepted:
            sys.exit("Invalid output")
        else:
            if input_ext == output_ext:
                try:
                    shirt = Image.open("shirt.png")
                    with Image.open(input) as input_iter:
                        input_cropped = ImageOps.fit(input_iter, shirt.size)
                        input_cropped.paste(shirt, mask = shirt)
                        input_cropped.save(output)
                except FileNotFoundError:
                    sys.exit("Input does not exist")
            else:
                sys.exit("Input and output have different extensions")
    else:
        if input_ext.find(".") == -1 and output_ext.find(".") != -1:
            sys.exit("Invalid input")
        elif input_ext.find(".") != -1 and output_ext.find(".") == 1:
            sys.exit("Invalid output")
        else:
            sys.exit("Invalid input and output")