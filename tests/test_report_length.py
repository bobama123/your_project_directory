from lib.report_length import *

def test_report_length_returns_correct_string_for_hello():
    result = report_length("hello")
    assert result == "This string was 5 characters long."
