from tabulate import tabulate
import sys
import csv

def main():
    if argv() == True:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                print(tabulate(reader, headers='keys', tablefmt='grid'))
        except FileNotFoundError:
            sys.exit('File not found !')


def argv():
    if len(sys.argv) == 2 and '.csv' in sys.argv[1]:
        return True
    elif len(sys.argv) > 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too many command-line arguments')
    else:
        sys.exit('not a csv file')

if __name__ == "__main__":
    main()