from validator_collection import checkers

def main():
    print(check_mail(input("Whats your email address ? ")))


def check_mail(mail):
    if checkers.is_email(mail):
        return 'Valid'
    else:
        return 'Invalid'


if __name__ == "__main__":
    main()