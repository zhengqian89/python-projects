from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("5/5") == 100
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("3/1")

    with pytest.raises(ZeroDivisionError):
        convert("7/0")

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"