
def main():
    lol = input()
    final = convert(lol)
    print(final)


def convert(lol):
    smile1 = lol.replace(':)', '🙂').replace(':(', '🙁')

    return smile1
main()