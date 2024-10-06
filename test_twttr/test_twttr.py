from twttr import shorten

def test_vowel():
    assert shorten("AeIoU") == ""

def test_consonant():
    assert shorten("BCDFG") == "BCDFG"

def test_number():
    assert shorten("Adam8") == "dm8"

def test_punctuation():
    assert shorten("Adam!!") == "dm!!"

def test_mixed():
    assert shorten("Adam") == "dm"