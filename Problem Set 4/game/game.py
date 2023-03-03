from random import randint


while True:
    try:
        level = int(input('level: '))

        if level <= 0:
            continue

        random = randint(1, level)
        break
    except ValueError:
        continue


while True:
    try:
        guess = int(input('Guess: '))

        if guess > 0:
            if guess < random:
                print('Too small!')

            elif guess > random:
                print('Too large!')

            else:
                print('Just right!')
                break

    except ValueError:
        continue

