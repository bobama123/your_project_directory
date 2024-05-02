import pytest
from lib.make_snippet import *


def test_for_returns_first_5_words_of_string():
    result = make_snippet("The first five words are hello my son is")
    assert result == "The first five words are ..."

def test_for_returns_error_when_string_is_none():
    with pytest.raises(Exception) as e:
        make_snippet(None)
    error_message = str(e.value)
    assert error_message == "No string set!"

def test_for_5_words():
    result = make_snippet("The first five words are")
    assert result == "The first five words are"


def test_for_empty():
    result = make_snippet("")
    assert result == ""