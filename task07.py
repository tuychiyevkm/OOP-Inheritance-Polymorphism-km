class Media:
    def __init__(self, title):
        self.title = title

    def play(self):
        pass

class Song(Media):
    def play(self):
        return f"Playing song: {self.title}"

class Movie(Media):
    def play(self):
        return f"Playing movie: {self.title}"

media_list = [Song("Believer"), Movie("Inception")]
for m in media_list:
    print(m.play())
