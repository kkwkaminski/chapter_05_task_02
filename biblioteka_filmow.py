class Media:
    def __init__(self, title, release_year, genre, play_count=0, *args, **kwargs):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.play_count = play_count

    def play(self):
        self.play_count += 1

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class Movie(Media):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return super().__str__()


class TVShow(Media):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02}E{self.episode:02} ({self.release_year})"


class MediaLibrary:
    def __init__(self):
        self.media_list = []

    def add_media(self, media):
        self.media_list.append(media)

    def display_media(self):
        for media in self.media_list:
            print(media)

if __name__ == "__main__":
    library = MediaLibrary()

    movie = Movie("Pulp Fiction", 1994, "Crime")
    tv_show = TVShow(1, 5, "The Simpsons", 1989, "Animation")

    library.add_media(movie)
    library.add_media(tv_show)


    movie.play()
    tv_show.play()


    library.display_media()