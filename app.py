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
# app.config["register_owner"] = mongo.db.owners.dog_image.insert_one()
# app.config["permitted_image_types"] = ["PNG", "JPG", "JPEG"]
# app.config["max_file_size"] = 0.5 * 1024 * 1024


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


@app.route("/sign_in_walker_page")
def sign_in_walker_page():
    return render_template("sign-in-walker.html")


@app.route("/sign_in_owner_page")
def sign_in_owner_page():
    return render_template("sign-in-owner.html")


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
            "owner_email": request.form.get("owner_email").lower(),
            "owner_location": request.form.get("owner_location").lower(),
            "preferred_age_group": request.form.get("preferred_age_group"),
            "dog_name": request.form.get("dog_name")
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


@app.route("/logout")
def logout():
    # remove user from session cookies
    session.pop("user")
    return redirect(url_for("sign_in"))


@app.route("/owner_profile/<owner_username>", methods=["GET", "POST"])
def owner_profile(owner_username):
    # Take session user's username from MongoDB
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
            walks=walks, owners=owners)

    return redirect(url_for("sign_in_owner"))


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
            "type_of_walk": request.form.get("type_of_walk")
        }
        mongo.db.walks.insert_one(add_walk)

        return redirect(url_for(
            "owner_profile", owner_username=session[
                "user"], walks=walk, owners=owners))
    return render_template("add-walk.html")


@app.route("/edit_walk/<walk_id>", methods=["GET", "POST"])
def edit_walk(walk_id):
    if request.method == "POST":
        submit = {
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.tasks.update({"_id": ObjectId(walk_id)}, submit)
        flash("Task Successfully Updated")

    walk = mongo.db.walks.find_one({"_id": ObjectId(walk_id)})
    return render_template("edit_task.html", walk=walk)



@app.route("/delete_walk/<walk_id>")
def delete_walk(walk_id):
    mongo.db.walks.remove({"_id": ObjectId(walk_id)})
    flash("Walk Successfully Deleted")
    return redirect(url_for("owner_profile", owner_username=session["user"]))


@app.route("/walker_profile/<walker_username>", methods=["GET", "POST"])
def walker_profile(walker_username):
    # Take session user's username from MongoDB
    walker = mongo.db.walkers.find_one(
        {"walker_username": session["user"]})
    owners = mongo.db.owners.find()
    walks = list(mongo.db.walks.find())
    if session["user"]:
        return render_template(
            "walker-profile.html",
            walker_username=walker_username,
            walker=walker, owners=owners, walks=walks)

    return redirect(url_for("sign_in_walker"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
