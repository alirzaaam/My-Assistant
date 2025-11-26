from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import requests


# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///todo.db")

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function



@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        new_task = request.form.get("new-task")
        date = datetime.now()
        # done = request.form.getlist("mycheck")
        # print(f"loooooooooooooooooooooooooooooooooooooooooooooooooooook: {done}")
        if not new_task:
            flash("New Task Field is Empthy")
            return redirect("/")
        else:
            db.execute("INSERT INTO jobs (id, job, date) VALUES (?, ?, ?)", session["user_id"], new_task, date)
            return redirect("/")
    else:
        data = db.execute("SELECT * FROM jobs WHERE id = ?", session["user_id"])
        api_key = "22386a71f263b516fd8bb35711a94926"
        my_city = db.execute("SELECT city FROM users WHERE id = ?", session["user_id"])

        result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={my_city[0]["city"]}&appid={api_key}")
        w_describtion = result.json()["weather"][0]["description"]
        w_temp = round((result.json()["main"]["temp"]) - 273.15)
        w_icon = result.json()["weather"][0]["icon"]

        if data:
            return render_template("index.html", task=data, icon=w_icon, temp=w_temp, desc=w_describtion.capitalize(), city=my_city[0]["city"].capitalize())
        else:
            return render_template("index.html", icon=w_icon, temp=w_temp, desc=w_describtion.capitalize(), city=my_city[0]["city"].capitalize())


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        conf_pass = request.form.get("confirmation")
        city = request.form.get("city")
        hash_pass = generate_password_hash(password)
        if not username:
            flash("Username Feild is Empty")
            return render_template("register.html")
        if len(username) <= 2 or len(username) > 10:
            flash("Username must be between 2 and 10 characters long.")
            return render_template("register.html")
        if not password:
            flash("Password Feild is Empty")
            return render_template("register.html")
        if not conf_pass:
            flash("Password Confirmation Feild is Empty")
            return render_template("register.html")
        if not city:
            flash("City Feild is Empty")
            return render_template("register.html")
        if password != conf_pass:
            flash("Password and Confirmation fileds do not match")
            return render_template("register.html")
        try:
            db.execute("INSERT INTO users (username, pass, city) VALUES (?, ?, ?)", username, hash_pass, city)

        except:
            flash("This User Exist!!")
            return render_template("register.html")
        flash("You Successfully Registered")
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username:
            flash("Must Provide Username")
            return render_template("login.html")
        if not password:
            flash("Must Provide Password")
            return render_template("login.html")

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        print(f'LOOOOOOOOOOOOOOOOOOOOOOOOOOOOK HEREEEEE: {rows}')
        if len(rows) != 1 or not check_password_hash(rows[0]["pass"], password):
            flash("Invalid Username and/or Password")
            return render_template("login.html")

        session["user_id"] = rows[0]["id"]

        return redirect("/")
    else:
        return render_template("login.html")



@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():

    my_city = db.execute("SELECT city FROM users WHERE id = ?", session["user_id"])
    data = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    username = data[0]["username"].capitalize()
    if request.method == "POST":
        old_pass = request.form.get("old_pass")
        new_pass = request.form.get("new_pass")
        conf_pass = request.form.get("conf_pass")
        new_city = request.form.get("new_city")
        db_hash = db.execute("SELECT pass FROM users WHERE id = ?", session["user_id"])
        render = redirect("/")


        if not old_pass:
            flash("Old Pass Field is Empty")
            return render
        if not new_pass:
            flash("New Pass Field is Empty")
            return render
        if not conf_pass:
            flash("Confirmation Pass Field is Empty")
            return render
        if new_pass != conf_pass:
            flash("New and Confirm Pass Are Not Same")
            return render
        if not new_city:
            flash("City Field is Empty")
            return render

        if not check_password_hash(db_hash[0]['pass'], old_pass):
            flash("Old Password Does Not Exist!!")
            return render
        else:
            try:
                db.execute("UPDATE users set pass = ? , city = ? WHERE id = ?", generate_password_hash(
                    new_pass,), new_city, session["user_id"])
            except:
                flash('Somthing Went Wrong')
                return redirect("/")
            flash('Your Password Successfully Changed')
            return redirect("/")

    else:

        return render_template("profile.html", city=my_city[0]["city"].capitalize(), username=username)

@app.route("/done", methods=["GET", "POST"])
@login_required
def done():
    data = db.execute("SELECT * FROM jobs WHERE id = ?", session["user_id"])

    if request.method == "POST":
            dl_item = request.form.get("option")
            if dl_item:
                db.execute(" DELETE FROM jobs WHERE job = ?", dl_item)
                flash('SUCCESSFULLY DELETED')
                return redirect("/")
            else:
                flash('Error: No item selected')
                return redirect("/")
    else:
        return render_template("done.html", task=data)

