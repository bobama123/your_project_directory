import pytest
from lib.password_checker import *

def test_password_checker_for_length_10():
    password_checker = PasswordChecker()
    result = password_checker.check("hellobobby")
    assert result == True


def test_password_checker_for_length_7():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("hellobo")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."