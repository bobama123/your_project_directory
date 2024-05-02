import pytest
from lib.grammar_stats import GrammarStats

"""
Given a text
#check returns True for capital letter and ends with punctuation mark
"""

def test_for_true_for_both_cases():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, my name is Bobby!")
    assert result == True

"""
Given a text
#check returns False for no capital letter and not ends with punctuation mark
"""

def test_for_false_for_both_cases():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hello, my name is Bobby")
    assert result == False

"""
Given a text
#check returns False for capital letter and not ends with punctuation mark
"""

def test_for_false_for_no_punctuation_ending():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, my name is Bobby")
    assert result == False

"""
Given a text
#check returns False for no capital letter and ends with punctuation mark
"""

def test_for_false_for_no_capital_letter():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hello, my name is Bobby?")
    assert result == False

"""
Given a text
#check raises error for empty text"
"""

def test_for_error_for_empty_text():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        result = grammar_stats.check("")
    error_message = str(e.value)
    assert error_message == "No text given"


"""
Given a text
#check returns 100% for all passing
"""

def test_for_all_passed():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Hello, my name is Bobby?")
    assert grammar_stats.check("Hello, my name is Bobby!")
    assert grammar_stats.check("Hello, my name is Bobby?")
    assert grammar_stats.check("Hello, my name is Bobby.")
    assert grammar_stats.check("Hello, my name is Bobby?")
    assert grammar_stats.percentage_good() == f"{100}%"



