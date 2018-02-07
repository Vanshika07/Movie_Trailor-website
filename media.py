import webbrowser
# sample


class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, movie_image, youtube_trailor):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_image
        self.trailer_youtube_url = youtube_trailor

    def show_trailor(self):
        webbrowser.open(self.trailer_youtube_url)
