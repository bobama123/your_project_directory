import pytest
from lib.diary import Diary

"""
Initially
There are no diary entries
"""

def test_initially_has_no_diary_entries():
    diary = Diary()
    assert diary.all() == []


"""
Initially
There are no words as no diary entries in all diary entries
"""

def test_initially_has_no_words_as_no_diary_entries():
    diary = Diary()
    assert diary.count_words() == 0


"""
Inititally, #reading_time should raise an error
"""

def test_initially_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(2)
    error = str(e.value)
    assert error == "No entries added yet"

"""
Inititally, #find_best_entry_for_reading_time should raise an error
"""

def test_initially_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(2, 1)
    error = str(e.value)
    assert error == "No entries added yet"