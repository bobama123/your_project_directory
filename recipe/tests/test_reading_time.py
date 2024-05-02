from lib.reading_time import *

def test_with_empty_string():
    assert reading_time("") == "0 seconds"

def test_with_2_words():
    result = reading_time("Hello World")
    assert result == "0.6 seconds"

def test_with_5_words():
    result = reading_time("Hello World, I am here")
    assert result == "1.5 seconds"