from um import count

def test():
    assert count("Um...") == 1
    assert count('yummy') == 0
    assert count("um, hello, um, world  ") == 2

