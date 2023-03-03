import sys

def main():
    if argv() == True:
        try:
            with open(sys.argv[1], 'r') as file:
                number_lines = 0
                for lines in file:
                    if space(lines) == True:
                        number_lines += 1
            print(number_lines)

        except FileNotFoundError:
            sys.exit('File not found !')


def space(lines):
    if not lines.lstrip().startswith("#") and lines.lstrip() != '':
        return True


def argv():
    if len(sys.argv) == 2 and '.py' in sys.argv[1]:
        return True
    elif len(sys.argv) > 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too many command-line arguments')
    else:
        sys.exit('Not Python file')

main()
