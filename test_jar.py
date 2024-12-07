from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        Jar(-3)
    with pytest.raises(ValueError):
        Jar(3.5)

def test_deposit():
    jar = Jar(5)
    jar.deposit(4)
    assert jar.size ==4
    with pytest.raises(ValueError):
        jar.deposit(2)

