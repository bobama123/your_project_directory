import pytest
from lib.present import *

def test_present_for_error_wrap_wrap():
    present = Present()
    present.wrap("choco")
    with pytest.raises(Exception) as e:
        present.wrap('hello')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."


def test_present_for_error_unwrap_empty():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."


def test_present_for_wrap_then_unwrap():
    present = Present()
    present.wrap("choco")
    assert present.unwrap() == "choco"
    

def test_present_for_wrap_wrap_then_unwrap():
    present = Present()
    present.wrap("choco")
    with pytest.raises(Exception) as e:
        present.wrap('hello')
    assert present.unwrap() == "choco"
