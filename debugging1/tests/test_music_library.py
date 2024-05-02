from lib.music_library import MusicLibrary
from lib.track import Track

"""
Initially
There are no tracks
"""

def test_initially_has_no_tracks():
    music_library = MusicLibrary()
    assert music_library.all() == []


"""
Initially
Searching for tracks gets an empty list
"""

def test_initially_searches_return_empty():
    music_library = MusicLibrary()
    assert music_library.search_by_title("hello") ==  []