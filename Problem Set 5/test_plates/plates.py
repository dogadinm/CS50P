def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if  len(s) >= 2 and len(s) <= 6:
        if s.isalpha()  or s[0:2].isalpha() and s[-2:].isnumeric()  and s[-2:][0] != "0":
            for c in s:
                if c in ['.', ' ', '!', '?',',']:
                    return False
            else:
                return True


    else:
        return False

if __name__ == "__main__":
    main()

