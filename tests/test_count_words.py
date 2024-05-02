import pytest
from lib.count_words import *

def test_for_empty_string():
    result = count_words("")
    assert result == 0

def test_for_5_words_in_a_string():
    result = count_words("Hello my name is Bobby")
    assert result == 5

def test_for_None():
    with pytest.raises(Exception) as e:
        count_words(None)
    error_message = str(e.value)
    assert error_message == "No string set!"


