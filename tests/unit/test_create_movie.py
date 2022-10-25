# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()

def test_feature_two():
    movies = movie_repository.get_all_movies()
    movie = movie_repository.create_movie('movie_title','movie_director','1')
    assert movie in movies
    assert movie.title == 'movie_title'
    assert movie.director == "movie_director"
    assert movie.rating == '1'
    
