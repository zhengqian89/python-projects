from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True

def test_no_alpha():
    assert is_valid("1989") == False

def test_no_0_as_first_no():
    assert is_valid("CS05") == False

def test_no_num_in_middle():
    assert is_valid("CS50P") == False

def test_start_with_at_least_2_chars():
    assert is_valid("H") == False

def test_no_punc():
    assert is_valid("PI3.14") == False

def test_min2_max6_char():
    assert is_valid("OUTATIME") == Falsem