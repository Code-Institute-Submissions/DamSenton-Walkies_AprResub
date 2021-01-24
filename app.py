import os
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


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/sign_in")
def sign_in():
    return render_template("sign-in.html")


@app.route("/sign_in_owner")
def sign_in_owner():
    return render_template("sign-in-owner.html")


@app.route("/sign_in_walker")
def sign_in_walker():
    return render_template("sign-in-walker.html")


@app.route("/register_owner")
def register_owner():
    return render_template("register-owner.html")


@app.route("/register_walker")
def register_walker():
    return render_template("register-walker.html")


if __name__ == "__main__":
    app.run(
       host=os.environ.get("IP", "0.0.0.0"),
       port=int(os.environ.get("PORT", "5000")),
       debug=True)