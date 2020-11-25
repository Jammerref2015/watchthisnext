import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_movies")
def get_movies():
    movies = list(mongo.db.movies.find())
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
        movie = {
            "title": request.form.get("title"),
            "synopsis": request.form.get("synopsis"),
            "genre": request.form.get("genre"),
            "platform": request.form.get("platform"),
            "rating": request.form.get("rating"),
            "release_year": request.form.get("release_year"),
            "ageRating": request.form.get("ageRating"),
            "movie_image": request.form.get("movie_image"),
            "created_by": session["user"]
        }
        mongo.db.movies.insert_one(movie)
        flash("Movie Successfully Added!!!")
        return redirect(url_for("addmovie"))

    return render_template("addmovie.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)