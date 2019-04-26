
import os
import csv
from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./movies.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Set up Flask debug
db = SQLAlchemy(app)
session = db.session

# Set up classes
class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64)) # Only unique title movies can exist in this data model
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))
    ratings_id = db.Column(db.Integer, db.ForeignKey('ratings.id'))

    def __repr__(self):
        return "{}".format(self.title)


class Director(db.Model):
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    movies = db.relationship('Movie',backref ='director', lazy = True)

    def __repr__(self):
        return "{} (ID: {})".format(self.name, self.id)

class Ratings(db.Model):
    __tablename__ = "ratings"
    id = db.Column(db.Integer, primary_key=True)
    imdb_rating = db.Column(db.Integer)
    movies = db.relationship('Movie', backref = 'rating', lazy = True)

##### Helper functions #####
def get_or_create_director(director_name):
    director = Director.query.filter_by(name=director_name).first()
    if director:
        return director
    else:
        director = Director(name=director_name)
        session.add(director)
        session.commit()
        return director

def create_rating(rate):
    rating = Ratings(imdb_rating=rate)
    session.add(rating)
    session.commit()
    return rating

##### Set up Controllers (route functions) #####

## Main route
@app.route('/')
def index(): ## When the main route is accessed, the program checks if there are any movies in the database. If none, it will import data from a csv file
    ## Import movie data from existing csv file
    with open("movies_clean.csv", "r", encoding = "utf-8") as f:
    	reader = csv.reader(f)
    	data = []
    	for i in reader:
    		data.append(i)
    if len(Movie.query.all()) == 0: ## If there are no movies at all
        for row in range (1, len(data)):
            director = get_or_create_director(data[row][12])
            rating = create_rating(data[row][14])
            movie = Movie(title = data[row][0], director_id = director.id, ratings_id = rating.id)
            session.add(movie)
            session.commit()

    return 'This is the main page. <br><a href="http://localhost:5000/allmovies">Click here to see the complete collection of movies. <br><a href="http://localhost:5000/alldirectors">Click here to see a complete list of directors. <br><a href = "http://localhost:5000/newmovie">Click here to add a new movie. <br><a href = "http://localhost:5000/director">Click here to search for the works of a specific director.'

## Route for displaying all the recorded movies
@app.route('/allmovies')
def allmovies():
    movies = Movie.query.all()
    num_movies = len(movies)
    directors = Director.query.all()
    return render_template('allmovies.html', allmovies = movies, alldirectors = directors, num_movies = num_movies)

## Route for displaing all the directors
@app.route('/alldirectors')
def alldirectors():
    directors = Director.query.all()
    num_directors = len(directors)
    return render_template('alldirectors.html', alldirectors = directors, num_directors = num_directors)

## Route for adding movies using a form
@app.route('/newmovie')
def addmovie_form():
    return render_template('addmovie.html')
## Route for getting data from the addmovie form, displaying the results, and saving the data to the database
@app.route('/newmovie_result',methods=["GET"])
def addmovies_result():
    if request.method == "GET":
        title = request.args.get('title','') # string
        director_name = request.args.get('director','') # string
        rate = request.args.get('rating','') # integer
        if Movie.query.filter_by(title = title).first(): # if there is a movie by that title
            return "That movie already exists, return to home page!"
        else: # Add movie, director and rating to database
            director = get_or_create_director(director_name)
            rating = create_rating(rate)
            movie = Movie(title = title, director_id = director.id, ratings_id = rating.id)
            session.add(movie)
            session.commit()
            return "New movie: <b>{}</b> by <b>{}</b>, rating: <b>{}</b>.".format(movie.title, director.name, rating.imdb_rating)

    return "Nothing was submitted yet... <a href='http://localhost:5000/form2'>Go submit something</a>"

## Route for searching for a director's works using a form
@app.route('/director')
def search_director():
    return render_template('searchdirector.html')

## Route for displaying a director and his/her complete list of movies
@app.route('/director_results', methods = ["GET"])
def show_director():
    if request.method == "GET":
        director_name = request.args.get('name','') # string
    if Director.query.filter_by(name = director_name).first():
        return "Director {} , movies: {}".format(get_or_create_director(director_name).name, get_or_create_director(director_name).movies)
    else:
        return "Director not found in database."

if __name__ == "__main__":
    db.create_all()
    app.run()
