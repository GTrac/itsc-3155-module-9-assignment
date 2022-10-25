# TODO: Feature 1
from flask.testing import FlaskClient
from app import app, create_movie
from src.models.movie import Movie

def test_display_page():
    test_app = app.test_client()
    response = test_app.get('/movies')
    assert b'<p class="mb-3">See our list of movie ratings below</p>' in response.data

def test_display_movie_title():
    test_app = app.test_client()
    response = test_app.get('/movies')
    assert b'<td id="movie" name = "movie">' in response.data

def test_display_movie_director():
    test_app = app.test_client()
    response = test_app.get('/movies')
    assert b'<td id="director" name = "director">' in response.data

def test_display_movie_rating():
    test_app = app.test_client()
    response = test_app.get('/movies')
    assert b'<td id="rating" name = "rating">' in response.data