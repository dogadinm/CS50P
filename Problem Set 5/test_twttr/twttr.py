def main():
    i = input('Input: ')
    print(shorten(i))


def shorten(word):
    a = 'aAeEiIoOuU'
    for q in a:
        word = word.replace(q,'')
    return(word)


if __name__ == "__main__":
    main()



