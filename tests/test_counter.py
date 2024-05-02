from lib.counter import *

def test_counts_for_user_so_far():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."