import pytest
from lib.music_listening import MusicListening
"""
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
"""

"""
Test for empty
Raise exception
"""

def test_for_no_tracks():
    music_listening = MusicListening()
    with pytest.raises(Exception) as e:
        music_listening.add("")
    error = str(e.value)
    assert error == "No tracks given"


"""
Test for 2 tracks given
returns list with 2 tracks
"""

def test_for_two_tracks():
    music_listening = MusicListening()
    music_listening.add("hello")
    music_listening.add("world")
    result = music_listening.format()
    assert result == ["hello", "world"]