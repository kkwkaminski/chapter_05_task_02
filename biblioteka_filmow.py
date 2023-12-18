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

    def get_movies(self):
        movies = [media for media in self.media_list if isinstance(media, Movie)]
        return sorted(movies, key=lambda x: x.title)

    def get_series(self):
        series = [media for media in self.media_list if isinstance(media, TVShow)]
        return sorted(series, key=lambda x: x.title)


if __name__ == "__main__":
    library = MediaLibrary()

    movie1 = Movie("Pulp Fiction", 1994, "Crime")
    movie2 = Movie("The Godfather", 1972, "Crime") 
    tv_show1 = TVShow(1, 5, "The Simpsons", 1989, "Animation")
    tv_show2 = TVShow(3, 4, "The Chosen", 2017, "Biblican")

    library.add_media(movie1)
    library.add_media(movie2)
    library.add_media(tv_show1)
    library.add_media(tv_show2)

    # Odtwarzamy tytuły
    movie1.play()
    tv_show1.play()

    # Wyświetlamy zawartość biblioteki
    library.display_media()

    # Wyświetlamy filmy
    print("\nFilmy:")
    for movie in library.get_movies():
        print(movie)

    # Wyświetlamy seriale
    print("\nSeriale:")
    for series in library.get_series():
        print(series)