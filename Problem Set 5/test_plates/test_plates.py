from plates import is_valid

def test1():
    assert is_valid('hello, world') == False
    assert is_valid('C') == False
    assert is_valid('CS50') == True
    assert is_valid("CS05") == False
    assert is_valid("csp50p") == False
    assert is_valid('50') == False
    assert is_valid("MYH,23") == False





