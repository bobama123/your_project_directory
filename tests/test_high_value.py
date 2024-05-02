from lib.high_value import *

def test_for_first_higher_than_second():
    highvalue = HighValue(5,-3)
    result = highvalue.get_highest()
    assert result == "First value is higher"


def test_for_first_lower_than_second():
    highvalue = HighValue(3,5)
    result = highvalue.get_highest()
    assert result == "Second value is higher"


def test_for_first_equal_to_second():
    highvalue = HighValue(3,3)
    result = highvalue.get_highest()
    assert result == "Values are equal"


def test_for_first_incresed_by_10():
    highvalue = HighValue(5,3)
    highvalue.add(10, "first")
    result = highvalue.get_highest()
    assert result == "First value is higher"

def test_add_first_value():
    highvalue = HighValue(5,3)
    highvalue.add(10, "first")
    assert highvalue.value_first == 15

def test_add_second_value():
    highvalue = HighValue(5,3)
    highvalue.add(10, "second")
    assert highvalue.value_second == 13

def test_for_second_incresed_by_10():
    highvalue = HighValue(5,3)
    highvalue.add(10, "second")
    result = highvalue.get_highest()
    assert result == "Second value is higher"

def test_for_both_incresed():
    highvalue = HighValue(5,3)
    highvalue.add(10, "second")
    highvalue.add(20, "first")
    result = highvalue.get_highest()
    assert result == "First value is higher"

def test_for_both_incresed_with_a_negative():
    highvalue = HighValue(5,3)
    highvalue.add(10, "second")
    highvalue.add(-2, "first")
    result = highvalue.get_highest()
    assert result == "Second value is higher"


    
    
    
