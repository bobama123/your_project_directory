from lib.string_builder import *

def test_creates_a_string_and_finds_size():
    string_builder = StringBuilder()
    string_builder.add("hello")
    result = string_builder.size()
    assert result == 5




def test_creates_a_string_and_returns_string():
    string_builder = StringBuilder()
    string_builder.add("hello")
    result = string_builder.output()
    assert result == "hello"