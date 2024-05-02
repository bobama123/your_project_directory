class MusicLibrary:
    # Public properties:
    #   tracks: a list of strings representing tracks

    def __init__(self):
        self._track = []

    def add(self, track):
        self._track.append(track)

    def all(self):
        return self._track
    
    def search_by_title(self, keyword):
        return [track for track in self._track if keyword in track.title]
