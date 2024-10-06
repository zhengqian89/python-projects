from um import count

def test_regular():
    assert count("Hi, um, I am Adam") == 1

def test_case():
    assert count("Hi, UM, I am Adam") == 1

def test_inword():
    assert count("Hi, yummy , I am Adam") == 0