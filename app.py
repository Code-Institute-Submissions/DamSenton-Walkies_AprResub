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

# connect the app to my database
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

# home page


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


# sign in as a walker
@app.route("/sign_in_walker_page")
def sign_in_walker_page():
    return render_template("sign-in-walker.html")


# sign in as an owner
@app.route("/sign_in_owner_page")
def sign_in_owner_page():
    return render_template("sign-in-owner.html")


# redirect to the general sign in page
@app.route("/sign_in")
def sign_in():
    return render_template("sign-in.html")


# register as an owner and push data to MongoDB
@app.route("/register_owner", methods=["GET", "POST"])
def register_owner():
    if request.method == "POST":
        # Checks to see if this username is already taken
        existing_owner = mongo.db.owners.find_one(
            {"owner_username": request.form.get("owner_username").lower()})
        existing_owner_email = mongo.db.owners.find_one(
            {"owner_email": request.form.get("owner_email").lower()})

        if existing_owner:
            flash("Username already exists")
            return redirect(url_for("register_owner"))

        if existing_owner_email:
            flash("Email is already in use")
            return redirect(url_for("register_walker"))

        register_owner = {
            "owner_username": request.form.get("owner_username").lower(),
            "owner_password": generate_password_hash(
                request.form.get("owner_password")),
            "owner_email": request.form.get("owner_email").lower(),
            "owner_location": request.form.get("owner_location").lower()
        }
        mongo.db.owners.insert_one(register_owner)

        # creates a new session cookie for the user
        session["user"] = request.form.get("owner_username").lower()
        return redirect(url_for(
            "owner_profile", owner_username=session["user"]))
    return render_template("register-owner.html")


# register as an walker and push data to MongoDB
@app.route("/register_walker", methods=["GET", "POST"])
def register_walker():
    if request.method == "POST":
        # Checks to see if this username is already taken
        existing_walker = mongo.db.walkers.find_one(
            {"walker_username": request.form.get("walker_username").lower()})
        existing_walker_email = mongo.db.walkers.find_one(
            {"walker_email": request.form.get("walker_email").lower()})

        if existing_walker:
            flash("Username already exists")
            return redirect(url_for("register_walker"))

        if existing_walker_email:
            flash("Email is already in use")
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
        return redirect(url_for("walker_profile",
                                walker_username=session["user"]))

    return render_template("register-walker.html")


# compare input with database to check if an owner can sign in
@app.route("/sign_in_owner", methods=["GET", "POST"])
def sign_in_owner():
    if request.method == "POST":
        # Checks to see if this username is already taken
        existing_owner = mongo.db.owners.find_one(
            {"owner_username": request.form.get("owner_username").lower()})

        if existing_owner:
            # Make sure passwords match
            if check_password_hash(
                    existing_owner[
                        "owner_password"], request.form.get("owner_password")):
                session["user"] = request.form.get(
                    "owner_username").lower()
                session["type"] = "owner"

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


# compare input with databse to check if a walker can sign in
@app.route("/sign_in_walker", methods=["GET", "POST"])
def sign_in_walker():
    if request.method == "POST":
        # Checks to see if this username is already taken
        existing_walker = mongo.db.walkers.find_one(
            {"walker_username": request.form.get("walker_username").lower()})

        if existing_walker:
            # Make sure passwords match
            if check_password_hash(
                    existing_walker[
                        "walker_password"], request.form.get(
                            "walker_password")):
                session["user"] = request.form.get(
                    "walker_username").lower()
                session["type"] = "walker"

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


# logs the user out
@app.route("/logout")
def logout():
    # remove user from session cookies
    session.pop("user")
    return redirect(url_for("sign_in"))


# takes data from my database and displays certain
#  information to the user based on below conditions
@app.route("/owner_profile/<owner_username>", methods=["GET", "POST"])
def owner_profile(owner_username):
    # Take session user's username from MongoDB
    walkers = mongo.db.walkers.find()
    owners = mongo.db.owners.find()
    walks = list(mongo.db.walks.find())
    owner_username = mongo.db.owners.find_one(
        {"owner_username": session["user"]})["owner_username"]
    result = mongo.db.walks.find()
    result_list = list(result)
    print(result_list)

    if session["user"]:
        return render_template(
            "owner-profile.html", owner_username=owner_username,
            walks=walks, owners=owners, walkers=walkers)

    return redirect(url_for("sign_in_owner"))


# takes user input and pushes data to my 'walks' collection
@app.route("/add_walk", methods=["GET", "POST"])
def add_walk():
    if request.method == "POST":
        owners = mongo.db.owners.find()
        walk = mongo.db.walks.find_one()
        # Add an owner's walk into MongoDb
        add_walk = {
            "owner_username": session["user"],
            "date_of_walk": request.form.get("date_of_walk"),
            "time_of_walk": request.form.get("time_of_walk"),
            "length_of_walk": request.form.get("length_of_walk"),
            "type_of_walk": request.form.get("type_of_walk"),
            "preferred_age_group": request.form.get("preferred_age_group"),
            "walk_location": request.form.get("walk_location").lower(),
            "dog_name": request.form.get("dog_name").lower(),
            "walk_email": request.form.get("walk_email")
        }
        mongo.db.walks.insert_one(add_walk)

        return redirect(url_for(
            "owner_profile", owner_username=session[
                "user"], walks=walk, owners=owners, add_walk=add_walk))
    return render_template("add-walk.html")


# takes data from 'walks' and allows this to be edited
@app.route("/edit_walk/<walk_id>", methods=["GET", "POST"])
def edit_walk(walk_id):
    if request.method == "POST":
        walk = mongo.db.walks.find_one()
        # Add an owner's walk into MongoDb
        submit = {
            "owner_username": session["user"],
            "date_of_walk": request.form.get("date_of_walk"),
            "time_of_walk": request.form.get("time_of_walk"),
            "length_of_walk": request.form.get("length_of_walk"),
            "type_of_walk": request.form.get("type_of_walk"),
            "preferred_age_group": request.form.get("preferred_age_group"),
            "walk_location": request.form.get("walk_location").lower(),
            "dog_name": request.form.get("dog_name").lower(),
            "walk_email": request.form.get("walk_email")
        }
        mongo.db.walks.update({"_id": ObjectId(walk_id)}, submit)

        return redirect(url_for(
            "owner_profile", owner_username=session[
                "user"], walks=walk))

    walk = mongo.db.walks.find_one({"_id": ObjectId(walk_id)})
    return render_template("edit-walk.html", walk=walk)


# takes data from 'walks' and allows it to be deleted
@app.route("/delete_walk/<walk_id>")
def delete_walk(walk_id):
    mongo.db.walks.remove({"_id": ObjectId(walk_id)})
    return redirect(url_for("owner_profile", owner_username=session["user"]))


# takes data from my database and displays
# certain information to the user based on below conditions
@app.route("/walker_profile/<walker_username>", methods=["GET", "POST"])
def walker_profile(walker_username):
    # Take session user's username from MongoDB
    walkers = list(mongo.db.walkers.find())
    walker = mongo.db.walkers.find_one(
        {"walker_username": session["user"]})
    walks = list(mongo.db.walks.find())
    owner_email = mongo.db.owners.find_one(
        {"owner_email": request.form.get("owner_email")})
    result = mongo.db.walks.find()
    result_list = list(result)
    print(result_list)
    if session["user"]:
        return render_template(
            "walker-profile.html",
            walker_username=walker_username,
            walker=walker, walks=walks,
            walkers=walkers, owner_email=owner_email)

    return redirect(url_for("sign_in_walker"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=False)
