import pytest
from jar import Jar

def test_init():
    jar = Jar(7)
    assert jar.volume == 7
    assert jar.cookies == 0


def test_str():
    jar = Jar()
    jar.deposit(8)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.cookies == 1


def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(7)
    assert jar.size == 1
