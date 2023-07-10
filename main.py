from imdb import IMDb
from imdb import Cinemagoer, IMDbError

ia = IMDb()

try:
# Obtener información sobre películas populares
    movies = ia.get_top250_movies()
    for movie in movies:
        peli = ia.get_movie(movie.getID())
        print(peli['genres'])
except IMDbError as e:
    print(e)