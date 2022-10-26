# TODO: Feature 2
import pytest
from app import app, create_movie

@pytest.fixture()
def client():
    client = create_movie('movie_title','movie_director','1')
    client.config.update({
        "TESTING" : True,
    })

    yield client

def test_feature_two(client):
    result = client.post('templates/create_movie_form.html', data = {
        "movie_name" : "movie_name",
        "movie_director" : "movie_director",
        "movie_rating" : "movie_rating"
    })

    follow_redirects = True

    assert result.status_code == 200

# Source : https://flask.palletsprojects.com/en/2.2.x/testing/#form-data