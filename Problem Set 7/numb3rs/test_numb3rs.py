from numb3rs import validate

def main():
    test()
    


def test():
    assert validate('255.255.255.255') == True
    assert validate('123.214.0.0') == True
    assert validate('1212.512.512.512') == False
    assert validate('1.223.334.400') == False
    assert validate('misha') == False



if __name__ == "__main__":
    main()