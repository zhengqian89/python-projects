from numb3rs import validate

def test_alpha():
    assert validate("cat") == False

def test_exceed():
    assert validate("300.3.6.28") == False

def test_v6():
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False

def test_less():
    assert validate("9.9.9") == False

def test_true():
    assert validate("123.123.123.123") == True

def test_first():
    assert validate("1.344.1.1") == False