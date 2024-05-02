from lib.greet import *

def test_greet_returns_bobby_for_name():
    result = greet("Bobby")
    assert result == "Hello, Bobby!"