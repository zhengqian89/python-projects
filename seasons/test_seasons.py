from seasons import convert
import pytest

def test_validity():
    with pytest.raises(SystemExit):
        convert("January 1, 1999")

def test_work():
    assert convert("2001-08-28") == 11589120