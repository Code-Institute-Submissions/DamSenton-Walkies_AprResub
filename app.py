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


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/sign_in")
def sign_in_user():
    return render_template("sign_in.html")


@app.route("/register_owner")
def register_owner():
    return render_template("register_owner.html")


@app.route("/register_walker")
def register_walker():
    return render_template("register_walker.html")


if __name__ == "__main__":
    app.run(
       host=os.environ.get("IP", "0.0.0.0"),
       port=int(os.environ.get("PORT", "5000")),
       debug=True)