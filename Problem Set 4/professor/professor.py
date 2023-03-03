from random import randint


def main():
    generate_integer(get_level())

def get_level():
    while True:
        level = input('Level: ')
        if level not in ['1','2','3']:
            continue
        return level


def generate_integer(level):
    score = 0
    for i in range(10):
        if level == '1':
            first_number = randint(0, 9)
            second_number = randint(0, 9)
        elif level == '2':
            first_number = randint(10, 99)
            second_number = randint(10, 99)
        else:
            first_number = randint(100, 999)
            second_number = randint(100, 999)

        health = 0
        while health <= 3:
            print(f'{first_number} + {second_number} = ', end='')
            answer = input()
            if answer == str(first_number + second_number):
                score += 1
                break
            elif answer != str(first_number + second_number) and health != 2:
                print('EEE')
                health += 1
                continue
            else:
                print('EEE')
                print(f'{first_number} + {second_number} = {first_number + second_number}')
                break
    print(score)

if __name__ == "__main__":
    main()