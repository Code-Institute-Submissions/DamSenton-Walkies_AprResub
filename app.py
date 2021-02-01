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


@app.route("/register_owner", methods=["GET", "POST"])
def register_owner():
    if request.method == "POST":
        # Checks to see if this username is already taken
        existing_owner = mongo.db.owners.find_one(
            {"owner_username": request.form.get("owner_username").lower()})

        if existing_owner:
            flash("Username already exists")
            return redirect(url_for("register_owner"))

        register_owner = {
            "owner_username": request.form.get("owner_username").lower(),
            "owner_password": generate_password_hash(
                request.form.get("owner_password")),
            "ownerr_email": request.form.get("owner_email").lower(),
            "owner_location": request.form.get("owner_location").lower(),
            "preferred_age_group": request.form.get("age_group")


        }
        mongo.db.owners.insert_one(register_owner)

        # creates a new session cookie for the user
        session["user"] = request.form.get("owner_username").lower()
        flash("Registration Successful!")
        return redirect(url_for(
            "owner_profile", owner_username=session["user"]))

    return render_template("register-owner.html")


@app.route("/register_walker", methods=["GET", "POST"])
def register_walker():
    if request.method == "POST":
        # Checks to see if this username is already taken
        existing_walker = mongo.db.walkers.find_one(
            {"walker_username": request.form.get("walker_username").lower()})

        if existing_walker:
            flash("Username already exists")
            return redirect(url_for("register_walker"))

        register_walker = {
            "walker_username": request.form.get("walker_username").lower(),
            "walker_password": generate_password_hash(
                request.form.get("walker_password")),
            "walker_email": request.form.get("walker_email").lower(),
            "walker_location": request.form.get("walker_location").lower(),
            "age_group": request.form.get("age_group")
        }
        mongo.db.walkers.insert_one(register_walker)

        # Create a new session cookie for the user
        session["user"] = request.form.get("walker_username").lower()
        flash("Registration Successful!")
        return redirect(url_for("walker_profile",
                                walker_username=session["user"]))

    return render_template("register-walker.html")


@app.route("/sign_in_owner", methods=["GET", "POST"])
def sign_in_owner():
    if request.method == "POST":
        # Checks to see if this username is already taken
        existing_user = mongo.db.owners.find_one(
            {"owner_username": request.form.get("owner_username").lower()})

        if existing_user:
            # Make sure passwords match
            if check_password_hash(
                    existing_user[
                        "owner_password"], request.form.get("owner_password")):
                session["user"] = request.form.get(
                    "owner_username").lower()
                session["type"] = "owner"
                # Here

                flash("Welcome, {}".format(request.form.get("owner_username")))
                return redirect(url_for(
                    "owner_profile", owner_username=session["user"]))

            else:
                # Invalid password input
                flash("Incorrect Username and/or Password")
                return redirect(url_for("sign_in_owner"))

        else:
            # Invalid username
            flash("Incorrect Username and/or Password")
            return redirect(url_for("sign_in_owner"))

    return render_template("sign-in-owner.html")


@app.route("/sign_in_walker", methods=["GET", "POST"])
def sign_in_walker():
    if request.method == "POST":
        # Checks to see if this username is already taken
        existing_user = mongo.db.walkers.find_one(
            {"walker_username": request.form.get("walker_username").lower()})

        if existing_user:
            # Make sure passwords match
            if check_password_hash(
                    existing_user[
                        "walker_password"], request.form.get(
                            "walker_password")):
                session["user"] = request.form.get(
                    "walker_username").lower()
                session["type"] = "walker"

                flash("Welcome, {}".format(
                    request.form.get("walker_username")))
                return redirect(url_for(
                    "walker_profile", walker_username=session["user"]))

            else:
                # Invalid password input
                flash("Incorrect Username and/or Password")
                return redirect(url_for("sign_in_walker"))

        else:
            # Invalid username
            flash("Incorrect Username and/or Password")
            return redirect(url_for("sign_in_walker"))

    return render_template("sign-in-walker.html")


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("sign_in"))


@app.route("/owner_profile/<owner_username>", methods=["GET", "POST"])
def owner_profile(owner_username):
    # Take session user's username from MongoDB
    owner_username = mongo.db.owners.find_one(
        {"owner_username": session["user"]})["owner_username"]

    if session["user"]:
        return render_template(
            "owner-profile.html", owner_username=owner_username)

    return redirect(url_for("sign_in_owner"))


@app.route("/walker_profile/<walker_username>", methods=["GET", "POST"])
def walker_profile(walker_username):
    # Take session user's username from MongoDB
    walker_username = mongo.db.walkers.find_one(
        {"walker_username": session["type"]})["walker_username"]

    if session["user"]:
        return render_template(
            "walker-profile.html", walker_username=walker_username)

    return redirect(url_for("sign_in_walker"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
