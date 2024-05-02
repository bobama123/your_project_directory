import pytest
from lib.check_text import *


def test_for_None():
    with pytest.raises(Exception) as e:
        check_text("")
    error_message = str(e.value)
    assert error_message == "No text set!"

def test_for_capital_letter_and_punctuation_at_end():
    result = check_text("Hello World!")
    assert result == True

def test_for_capital_letter_and_punctuation_in_text():
    result = check_text("Hello World, I am here")
    assert result == False

def test_for_no_capital_letter_and_punctuation_at_end():
    result = check_text("hello World, I am here")
    assert result == False

def test_for_no_capital_letter_and_no_punctuation_at_end():
    result = check_text("hello World, I am here")
    assert result == False


