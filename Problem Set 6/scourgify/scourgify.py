import sys
import csv

def main():


    if argv() == True:
        try:
            people =[]
            with open(sys.argv[1]) as file_before:
                reader = csv.DictReader(file_before)
                for row in reader:
                    name = row['name'].split(',')
                    house = row['house']
                    first_name = name[1].lstrip()
                    last_name = name[0]
                    people.append({'first': first_name , 'last': last_name, 'house': house})


            with open(sys.argv[2], 'w') as file_after:
                writer = csv.DictWriter(file_after, fieldnames=['first', 'last', 'house'])
                writer.writeheader()
                writer.writerows(people)

        except FileNotFoundError:
            sys.exit(f'Could bot read {sys.argv[1]}')


def argv():
    True
    if len(sys.argv) == 3 and  '.csv' in sys.argv[1]:
        return True
    elif len(sys.argv) < 3:
            sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
            sys.exit('Too many command-line arguments')
    else:
        sys.exit('not a csv file')

if __name__ == "__main__":
    main()




