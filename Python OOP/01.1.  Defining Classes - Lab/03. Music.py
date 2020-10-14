class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def get_info(self):
        return f'This is {self.title} from {self.artist}'

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics

music = Music('Title', 'Artist', 'Lyrics')
print(music.get_info())
print(music.print_info())
print(music.play())