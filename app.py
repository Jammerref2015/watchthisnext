import os
import random
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

# Quotes from movies randomised from this list. Displayed at random on log in.
quotes = [' "Do ya feel lucky? Well, do ya, punk". - Dirty Harry (1971)',
          '"May the force be with you." - Star Wars (1977)',
          '“I feel the need – the need for speed” - Top Gun (1986)',
          " 'I'll be right here'. - E.T. (1982)",
          '"Yippe-ki-yi-yay, Motherf**ker" - Die Hard (1988)',
          ' “At my signal, unleash hell” - Gladiator (2000)',
          " We're gonna need a bigger boat.' - Jaws (1977)"
        ]


@app.route("/")
@app.route("/get_movies")
def get_movies():
    movies = list(mongo.db.movies.find())
    return render_template("movies.html", movies=movies)


@app.route("/search")
def search():
    query = request.args.get("query")
    movies = list(mongo.db.movies.find({"$text": {"$search": query}}))
    return render_template("movies.html", movies=movies)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("get_movies"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                flash(quotes[random.randint(0, len(quotes)-1)])
                return redirect(url_for('get_movies',
                                        username=session["user"]))
            else:
                # incorrect password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/addmovie", methods=["GET", "POST"])
def addmovie():
    if request.method == "POST":

        existing_movie = mongo.db.movies.find_one(
            {"title": request.form.get("title")})

        if existing_movie:
            flash("Movie already exists")
            return redirect(url_for("addmovie"))

        movie = {
            "title": request.form.get("title"),
            "synopsis": request.form.get("synopsis"),
            "genre": request.form.get("genre"),
            "platform": request.form.get("platform"),
            "rating": request.form.get("rating"),
            "release_year": request.form.get("release_year"),
            "age_rating": request.form.get("age_rating"),
            "movie_image": request.form.get("movie_image"),
            "created_by": session["user"]
        }
        mongo.db.movies.insert_one(movie)
        flash("Movie Successfully Added!!!")
        return redirect(url_for("get_movies"))

    return render_template("addmovie.html")


@app.route("/delete_movie/<movie_id>")
def delete_movie(movie_id):
    mongo.db.movies.delete_one({"_id": ObjectId(movie_id)})
    flash("Movie successfully deleted!")
    return redirect(url_for("get_movies"))


@app.route("/movie/<movie_id>")
def movie(movie_id):
    movie_data = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    return render_template('movie.html', movie=movie_data)


@app.route("/edit_movie/<movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    if request.method == "POST":
        movie = {
            "title": request.form.get("title"),
            "synopsis": request.form.get("synopsis"),
            "genre": request.form.get("genre"),
            "platform": request.form.get("platform"),
            "rating": request.form.get("rating"),
            "release_year": request.form.get("release_year"),
            "age_rating": request.form.get("age_rating"),
            "movie_image": request.form.get("movie_image"),
            "created_by": session["user"]
        }
        mongo.db.movies.update({"_id": ObjectId(movie_id)}, movie)
        flash('Movie successfully edited!')
        return redirect(url_for("get_movies"))

    movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    return render_template("edit_movie.html", movie=movie)


@app.route("/logout")
def logout():
    flash('You have successfully logged out.')
    session.pop("user")
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 8000)),
            debug=True)
