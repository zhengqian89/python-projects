from jar import Jar
import pytest

def test_init():
    jar = Jar()

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.deposit(9)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    with pytest.raises(ValueError):
        jar.deposit(100)

def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.withdraw(100)