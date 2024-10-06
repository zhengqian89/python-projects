from bank import value

def test_Hello():
    assert value("Hello") == 0

def test_hello():
    assert value("hello") == 0

def test_h_nothello():
    assert value("hey") == 20

def test_anything_else():
    assert value("What's up!") == 100