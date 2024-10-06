from working import convert
import pytest

def test_notrailing():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_trailing():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_apm():
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"

def test_12apm():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_apm():
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")

def test_wrongH():
    with pytest.raises(ValueError):
        convert("18:00 AM to 4:00 PM")

def test_wrongM():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")

def test_wrongSEMI():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")