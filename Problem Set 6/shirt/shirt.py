import sys
from PIL import Image, ImageOps
from os import path


def main():
    if argv() == True:
        extensions_format = ['.jpg', '.jpeg', '.png']
        extensions1 = path.splitext(sys.argv[1])
        extensions2 = path.splitext(sys.argv[2])

        if extensions1[1] and extensions2[1] not in extensions_format:
            sys.exit('Wrong extensions')

        elif extensions1[1] != extensions2[1]:
            sys.exit('input and output have different extensions')
            
        else:
            try:
                image = Image.open(sys.argv[1])
                shirt = Image.open('shirt.png')

                image = ImageOps.fit(image, shirt.size)
                image.paste(shirt, None, shirt)
                image.save(sys.argv[2])

            except FileNotFoundError:
                sys.exit('File doest exit')


def argv():
    if len(sys.argv) == 3:
        return True
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')


if __name__ == "__main__":
    main()
