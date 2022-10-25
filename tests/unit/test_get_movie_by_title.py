# TODO: Feature 3
from app import app, create_movie
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository
 
def test_get_movie_by_title():
    test_app = app.test_client()
    response = test_app.get('/movies/search')
    assert b'<div class="form-group">'in response.data


def test_get_movie_with_None():
    test_app = app.test_client()
    response = test_app.get('/movies/search?search=Star+Wars')
    assert b'Star Wars not found! try a different search' in response.data
    assert not b'<table class="table">'in response.data


def test_get_movie_with_Movie():
    test_app = app.test_client()
    with test_app.application.app_context():
        movieRepo = get_movie_repository()
        movieRepo.create_movie('Star Wars', 'George Lucas', 5)
    #test_app.application.view_functions
    response = test_app.get('/movies/search?search=Star+Wars')
    assert b'One result matching' in response.data
    assert b'<table class="table">'in response.data
    assert b'<th scope="col">Star Wars</th>' in response.data
    assert b'<th scope="col">George Lucas</th>' in response.data
    assert b'<th scope="col">5</th>' in response.data

    