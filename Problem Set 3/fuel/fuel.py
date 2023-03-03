def main():
    i = fuel()

    if i >= 0.99:
        print('F')

    elif i <= 0.01:
        print('E')

    else:
        print(f'{round(i*100)}%')


def fuel():
    while True:
        try:
            xy = input('Fraction: ')
            x,y = xy.split('/')


            if int(y)>=int(x):
                if y != 0:
                    return int(x)/int(y)

        except(ValueError, ZeroDivisionError):
            pass

main()