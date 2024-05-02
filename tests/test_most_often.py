from lib.most_often import *


def tests_for_clear_winner():
    most_often = MostOften([1, 1, 2, 2, 2, 3, 3])
    most_often.add_new(5)
    assert most_often.get_most_often() == 2

def tests_for_no_clear_winner_with_negatives():
    most_often = MostOften([-1, -1, 2, 2, 2, 3, 3])
    most_often.add_new(-1)
    assert most_often.get_most_often() == "no clear winner"

def tests_for_clear_winner_with_negatives_and_positive():
    most_often = MostOften([-1, 1, 2, 2, 2, 3, 3])
    most_often.add_new(-1)
    assert most_often.get_most_often() == 2

def tests_for_clear_winner_with_multiple_values():
    most_often = MostOften([-1, -1, 2, 2, 2, 3, 3, 3, 3])
    most_often.add_new(-1)
    assert most_often.get_most_often() == 3

def tests_for_clear_winner_with_empty_list():
    most_often = MostOften([])
    most_often.add_new(1)
    assert most_often.get_most_often() == 1

def tests_for_no_clear_winner_with_multiple_numbers():
    most_often = MostOften([-1, 1, 2, 2, 2, 3, 3])
    most_often.add_new(-1)
    most_often.add_new(-1)
    assert most_often.get_most_often() == "no clear winner"






