from cgitb import text
from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    movie_list=movie_repository.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, movie_list=movie_list)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)



@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    movie_title = request.form.get('movie_name')
    movie_director = request.form.get('movie_director')
    movie_rating = request.form.get('movie_rating')
    
    movie_repository.create_movie(movie_title, movie_director, int(movie_rating))

    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    #get movie title,
    movieSearch = request.args.get('search')
    message = ''
    #search by movie in database
    try:
        movie = movie_repository.get_movie_by_title(movieSearch)
        movieTitle = movie.title
        movieDirector = movie.director
        movieRating = movie.rating
        showTable = True
        showMessage = True
        message = 'One result matching "{0}"'.format(movieSearch)
    except:
        message = '{0} not found! try a different search'.format(movieSearch)
        movieTitle = ''
        movieDirector = '' 
        movieRating = ''
        showTable = False
        if movieSearch == None or movieSearch == '':
            showMessage = False
        else:
            showMessage = True
    finally:
    #return results 
        return render_template(
            'search_movies.html', 
            search_active=True, 
            showTable = showTable, 
            message = message, 
            movieTitle = movieTitle, 
            movieDirector = movieDirector, 
            movieRating = movieRating,
            showMessage = showMessage)
