import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
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


@app.route("/owner_info")
def owner_info():
    info = list(mongo.db.owners.find())
    return render_template("walker-profile.html", owners=info)


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
            "ownerr_email": request.form.get("owner_email").lower(),
            "owner_location": request.form.get("owner_location").lower(),
            "preferred_age_group": request.form.get("preferred_age_group")
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
        {"walker_username": session["user"]})["walker_username"]
    walkers = mongo.db.walkers.age_group
    owners = mongo.db.owners.preferred_age_group
    if session["user"]:
        return render_template(
            "walker-profile.html",
            walker_username=walker_username, walkers=walkers, owners=owners)

    return redirect(url_for("sign_in_walker"))


app.config["image_uploads"] = "/workspace/Walkies/static/uploads"
app.config["permitted_image_types"] = ["PNG", "JPG", "JPEG"]
app.config["max_file_size"] = 0.5 * 1024 * 1024


def permitted_image(filename):
    if "." not in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["permitted_image_types"]:
        return True
    else:
        return False


def permitted_file_size(filesize):
    if int(filesize) <= app.config["max_file_size"]:
        return True
    else:
        return False


@app.route("/upload_image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            # if "filesize" in request.cookies:

            #     if not permitted_file_size(request.cookies["filesize"]):
            #         print("Filesize exceeded maximum limit")
            #         return redirect(url_for(
            #             "owner_profile", owner_username=mongo.db.owners.find_one(
            #                 {"owner_username": session[
            #                     "user"]})["owner_username"]))

            image = request.files["image"]

            if image.filename == "":
                print("No filename")
                return redirect(url_for(
                    "owner_profile", owner_username=mongo.db.owners.find_one(
                        {"owner_username": session[
                            "user"]})["owner_username"]))

            if permitted_image(image.filename):
                filename = secure_filename(image.filename)

                image.save(os.path.join(
                    app.config["image_uploads"], filename))

                print("Image saved")

                return redirect(url_for(
                    "owner_profile", owner_username=mongo.db.owners.find_one(
                        {"owner_username": session[
                            "user"]})["owner_username"]))

            else:
                print("That file extension is not allowed")
                return redirect(url_for(
                    "owner_profile", owner_username=mongo.db.owners.find_one(
                        {"owner_username": session[
                            "user"]})["owner_username"]))

    return render_template("owner-profile.html")


# @app.route("/upload_image", methods=["GET", "POST"])
# def upload_image():
#     # Upload Image to workspace
#     if request.method == "POST":
#         if request.files:
#             image = request.files["image"]
#             image_result = permitted_image(image.filename)
#             if image.filename == "":
#                 flash("Image must have a filename")
#                 return redirect(url_for(
#                     "owner_profile", owner_username=mongo.db.owners.find_one(
#                         {"owner_username": session[
#                             "user"]})["owner_username"]))
#             if image_result is False:
#                 flash("Image type is not supported")
#             return redirect(url_for(
#                 "owner_profile", owner_username=mongo.db.owners.find_one(
#                     {"owner_username": session["user"]})["owner_username"]))

#         else:
#             filename = secure_filename(image.filename)

#             image.save(os.path.join(
#                 app.config["image_uploads"], filename))

#             flash("Image Succesfully Uploaded")
#             return redirect(url_for(
#                 "owner_profile", owner_username=mongo.db.owners.find_one(
#                     {"owner_username": session["user"]})["owner_username"]))

#     return render_template("owner-profile.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)


# return redirect(url_for(
#                     "owner_profile", owner_username=mongo.db.owners.find_one(
#                         {"owner_username": session[
#                             "user"]})["owner_username"]))
