import media
import fresh_tomatoes
# These are different movies their discription,poster link and youtube url
# Movie instances are created in the following code using media.Movie()
beeth = media.Movie(
                    "BEETHOVEN",
                    "A story of a boy and his beloved dog",
                    "http://img.moviepostershop.com/beethovens-5th-movie-poster-2003-1020454520.jpg",
                    "https://www.youtube.com/watch?v=ki8wHMR-yOI"
                    )


eigh = media.Movie(
                    "EIGHT BELOW",
                    "story of eight husky's",
                    "http://sunny.fm/wp-content/uploads/2013/12/eight-below-dvd-poster_41277377.jpg",
                    "https://www.youtube.com/watch?v=zz7TGf1awDo"
                    )

hach = media.Movie(
                    "HACHIKO",
                    "a dog's tale",
                    "http://pad.mymovies.it/filmclub/2009/05/073/locandina.jpg",
                    "https://www.youtube.com/watch?v=Y6U7mAnPtw4"
                   )

dal = media.Movie(
                    "101 DALMATIONS",
                    "Story of 101 dalmations",
                    "https://passpopcorn.files.wordpress.com/2013/04/101-dalmatians-_1961_.jpg",
                    "https://www.youtube.com/watch?v=4PU6wMl7R80"
                  )

mar = media.Movie(
                    "MARLEY & ME",
                    "The naughty Labrador",
                    "https://cdn.traileraddict.com/content/20th-century-fox/marleyandme-6.jpg",
                    "https://www.youtube.com/watch?v=0UMMGNxg1Lg"
                    )

snw = media.Movie(
                    "SNOW DOGS",
                    "the Husky's",
                    "https://image.tmdb.org/t/p/original/xhfXTGQ8Y0CSCuMCFRO1kCUZZYv.jpg",
                    "https://www.youtube.com/watch?v=8mao0cFzm8I")
# An array of movie instances is created
movies = [beeth, eigh, hach, dal, mar, snw]
fresh_tomatoes.open_movies_page(movies)  # The movie page opening is initiated
