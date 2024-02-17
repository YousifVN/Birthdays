import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

def removing_spam(id):
    db.execute("DELETE FROM birthdays WHERE id = ?", id)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        
        if not name:
            feedback = "You must enter a name"
            return render_template("feedback.html", feedback=feedback)

        if not month:
            feedback = "You must enter a month"
            return render_template("feedback.html", feedback=feedback)

        if not day:
            feedback = "You must enter a day"
            return render_template("feedback.html", feedback=feedback)

        db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", name, month, day)

        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        rows = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays=rows)

# removing_spam(8)
# removing_spam(6)
# removing_spam(7)