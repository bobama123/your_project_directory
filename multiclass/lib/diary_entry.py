import math
class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("No entry")
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("No words")
        return math.ceil(self.count_words()/wpm)

    def reading_chunk(self, wpm, minutes):
        words_can_read = wpm * minutes
        all_content_words = self.contents.split()
        if self.read_so_far >= len(all_content_words):
            self.read_so_far = 0
        
        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + words_can_read
        readable_chunk = all_content_words[chunk_start:chunk_end]
        self.read_so_far = chunk_end
        return " ".join(readable_chunk)
