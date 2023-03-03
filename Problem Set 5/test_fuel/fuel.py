
def main():
    xy = input('Fraction: ')
    i = convert(xy)
    print(gauge(i))

def convert(xy):
    while True:
        x,y = xy.split('/')
        try:

            if int(y)>=int(x):
                if y != 0:
                    return int(x)/int(y)

        except (ValueError, ZeroDivisionError):
            pass



def gauge(i):


    if i >= 0.99:
        return'F'

    elif i <= 0.01:
        return'E'

    else:
        return f'{round(i*100)}%'


if __name__ == "__main__":
    main()