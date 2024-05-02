import pytest
from lib.diary_entry import DiaryEntry


"""
Given a title and contents
#count_words returns the number of words:
"""

def test_counts_words_in_entry():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.count_words()
    assert result == 2

"""
Given an empty title and contents
#count_words raises an error:
"""

def test_errors_on_empty():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "")
    error_message = str(e.value)
    assert error_message == "No entry"


"""
Given a wpm of 2
And a text with 2 words
#reading_time returns 1 minute
"""

def test_reading_time_two_wpm_and_two_words():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.reading_time(2)
    assert result == 1

"""
Given a wpm of 2
And a text with 3 words
#reading_time returns 2 minute
"""

def test_reading_time_two_wpm_and_three_words():
    diary_entry = DiaryEntry("My Title", "Some contents are")
    result = diary_entry.reading_time(2)
    assert result == 2

"""
Given a wpm of 0
#reading_time raises and error
"""

def test_reading_time_0_words():
    diary_entry = DiaryEntry("My Title", "Some contents")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    error_message = str(e.value)
    assert error_message == "No words"


"""
Given a contents of 4 words
Given a wpm of 2 and a minutes of 1
#reading_chunk returns the first 2 words of the string
e.g. Some contents
"""

def test_reading_chunk_two_wpm_and_one_word():
    diary_entry = DiaryEntry("My Title", "Some contents are me")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "Some contents"


"""
Given a contents of 4 words
Given a wpm of 2 and a minutes of 1
First time, #reading_chunk returns the first 2 words of the string
e.g. Some contents
Next time, the next 2 words
e.g. are me
"""

def test_reading_chunk_two_wpm_and_one_word_twice():
    diary_entry = DiaryEntry("My Title", "Some contents are me")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "Some contents"
    result = diary_entry.reading_chunk(2, 1)
    assert result == "are me"


"""
Given a contents of 3 words
Given a wpm of 2 and a minutes of 1
First time, #reading_chunk returns the first 2 words of the string
e.g. Some contents
Next time, the next 2 words
e.g. are
Next time, loop back to the start.
e.g. Some contents
"""

def test_reading_chunk_two_wpm_and_one_word_looped():
    diary_entry = DiaryEntry("My Title", "Some contents are")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "Some contents"
    result = diary_entry.reading_chunk(2, 1)
    assert result == "are"
    result = diary_entry.reading_chunk(2, 1)
    assert result == "Some contents"


"""
Given a contents of 4 words
Given a wpm of 2 and a minutes of 1
First time, #reading_chunk returns the first 2 words of the string
e.g. Some contents
Next time, the next 2 words
e.g. are me
Next time, loop back to the start.
e.g. Some contents
"""

def test_reading_chunk_two_wpm_and_one_word_looped_with_exact_ending():
    diary_entry = DiaryEntry("My Title", "Some contents are me")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "Some contents"
    result = diary_entry.reading_chunk(2, 1)
    assert result == "are me"
    result = diary_entry.reading_chunk(2, 1)
    assert result == "Some contents"