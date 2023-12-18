class MediaLibrary:
    def __init__(self):
        self.media_list = []

    def add_media(self, media):
        self.media_list.append(media)

    def display_media(self):
        for media in self.media_list:
            print(media)

    def get_movies(self):
        return sorted([media for media in self.media_list if isinstance(media, Movie)], key=lambda x: x.title)

    def get_series(self):
        return sorted([media for media in self.media_list if isinstance(media, TVShow)], key=lambda x: x.title)

    def search(self, title):
        return [media for media in self.media_list if media.title.lower() == title.lower()]


class Movie:
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.play_count = 0

    def play(self):
        self.play_count += 1

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class TVShow:
    def __init__(self, season, episode, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.season = season
        self.episode = episode
        self.play_count = 0

    def play(self):
        self.play_count += 1

    def __str__(self):
        return f"{self.title} S{self.season:02d}E{self.episode:02d} ({self.release_year})"


if __name__ == "__main__":
    library = MediaLibrary()

    movie1 = Movie("Pulp Fiction", 1994, "Crime")
    movie2 = Movie("The Godfather", 1972, "Crime")
    tv_show1 = TVShow(1, 5, "The Simpsons", 1989, "Animation")
    tv_show2 = TVShow(2, 10, "Breaking Bad", 2008, "Drama")

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

    # Wyszukujemy tytuł
    search_title = "The Simpsons"
    search_results = library.search(search_title)
    print(f"\nWyszukiwanie dla '{search_title}':")
    for result in search_results:
        print(result)