import random

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

    def generate_views(self):
        if self.media_list:
            selected_media = random.choice(self.media_list)
            views = random.randint(1, 100)
            selected_media.play_count += views

    def generate_views_multiple_times(self, times=10):
        for _ in range(times):
            self.generate_views()

    def top_titles(self, num_titles=5, content_type=None):
        if content_type == 'movies':
            sorted_media = sorted([media for media in self.media_list if isinstance(media, Movie)],
                                  key=lambda x: x.play_count, reverse=True)
        elif content_type == 'series':
            sorted_media = sorted([media for media in self.media_list if isinstance(media, TVShow)],
                                  key=lambda x: x.play_count, reverse=True)
        else:
            sorted_media = sorted(self.media_list, key=lambda x: x.play_count, reverse=True)

        return sorted_media[:num_titles]


class Movie:
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.play_count = 0

    def play(self):
        self.play_count += 1

    def __str__(self):
        return f"{self.title} ({self.release_year}) - {self.play_count} views"


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
        return f"{self.title} S{self.season:02d}E{self.episode:02d} ({self.release_year}) - {self.play_count} views"


if __name__ == "__main__":
    library = MediaLibrary()

    movie1 = Movie("Pulp Fiction", 1994, "Crime")
    movie2 = Movie("The Godfather", 1972, "Crime")
    movie3 = Movie("Titanic", 1997, "Drama")
    tv_show1 = TVShow(1, 5, "The Simpsons", 1989, "Animation")
    tv_show2 = TVShow(3, 4, "The Chosen", 2017, "Biblical")
    tv_show3 = TVShow(2, 10, "Breaking Bad", 2008, "Drama")


    library.add_media(movie1)
    library.add_media(movie2)
    library.add_media(tv_show1)
    library.add_media(tv_show2)

    # Odtwarzamy tytuły
    movie1.play()
    tv_show1.play()

    # Generujemy odtworzenia
    library.generate_views_multiple_times()

    # Wyświetlamy zawartość biblioteki
    library.display_media()

    # Wyświetlamy top filmy
    print("\nTop Filmy:")
    for top_movie in library.top_titles(num_titles=2, content_type='movies'):
        print(top_movie)

    # Wyświetlamy top seriale
    print("\nTop Seriale:")
    for top_series in library.top_titles(num_titles=2, content_type='series'):
        print(top_series)