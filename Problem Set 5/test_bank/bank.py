def main():
    greeting = input('say: ')
    i = value(greeting)
    print('$' + i)


def value(greeting):
    greeting = greeting.lower().strip()

    if 'Hello' and 'hello' in greeting:
        return 0

    elif 'H' == greeting[0] or 'h' == greeting[0]:
        return 20

    else:
        return 100



if __name__ == "__main__":
    main()
