from lib.diary_entry import DiaryEntry
from lib.diary import Diary


"""
Given I add two diary entries
I can see them represented in the list
"""

def test_adds_multiple_diary_entries_and_lists_them():
    diary = Diary()
    diary_entry1 = DiaryEntry("Hello", "This world is mine")
    diary_entry2 = DiaryEntry("Bye", "The world is not mine")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.all() == [diary_entry1, diary_entry2]

"""
Given I add two diary entries
And call #count_words
I get sum of all words in contents of the diary entries
"""

def test_adds_multiple_diary_entries_and_counts_word_of_them():
    diary = Diary()
    diary_entry1 = DiaryEntry("Hello", "This world is mine")
    diary_entry2 = DiaryEntry("Bye", "The world is not mine")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.count_words() == 9


"""
Given a wpm of 2
And 2 entries with 9 words altogether
#reading_time returns 5 minutes
"""

def test_adds_multiple_diary_entries_and_gives_reading_time_for_two_wpm():
    diary = Diary()
    diary_entry1 = DiaryEntry("Hello", "This world is mine")
    diary_entry2 = DiaryEntry("Bye", "The world is not mine")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.reading_time(2) == 5


"""
Given I add two diary entries, one long and one short
And i call #find_best_entry_for_reading_time
With a wpm and minutes that mean i can only read the short one
Then #find_best_entry_for_reading_time returns the shorter one
"""

def test_finds_best_entry_for_reading_time_that_fits_in_time():
    diary = Diary()
    diary_entry1 = DiaryEntry("Hello", "This world is mine")
    diary_entry2 = DiaryEntry("Bye", "The world is not mine, I am cool")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.find_best_entry_for_reading_time(2, 3) == diary_entry1

"""
Given I add two diary entries, one long and one short
And i call #find_best_entry_for_reading_time
With a wpm and minutes that mean i cannot read that entry
Then #find_best_entry_for_reading_time returns None
"""

def test_finds_best_entry_for_reading_time_returns_none():
    diary = Diary()
    diary_entry1 = DiaryEntry("Hello", "This world is mine")
    diary_entry2 = DiaryEntry("Bye", "The world is not mine, I am cool")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.find_best_entry_for_reading_time(2, 1) == None


"""
Given I add two diary entries, one long and one short
And i call #find_best_entry_for_reading_time
With a wpm and minutes that mean i could read both
Then #find_best_entry_for_reading_time returns the longer one
"""

def test_finds_longer_entry_for_reading_time_that_fits_in_time():
    diary = Diary()
    diary_entry1 = DiaryEntry("Hello", "This world is mine")
    diary_entry2 = DiaryEntry("Bye", "The world is not mine, I am cool")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.find_best_entry_for_reading_time(2, 5) == diary_entry2


