import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    pattern = re.search(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$', ip)

    if pattern:
        for group in pattern.groups():

            if int(group) <= 255 and int(group) >= 0:
                continue
            else:
                return False
        return True

    else:
        return False


if __name__ == "__main__":
    main()