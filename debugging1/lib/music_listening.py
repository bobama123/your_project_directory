class MusicListening():
    def __init__(self):
        self.music_list = []

    def add(self, track):
        if track == "":
            raise Exception("No tracks given")
        else:
            self.music_list.append(track)
        
    def format(self):
        return self.music_list