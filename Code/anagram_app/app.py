from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def get_input():
    """Show form for user to input a string to make anagrams from (a word)."""
    return render_template("form.html")


@app.route("/word")
def parse_data():
    return redirect(url_for("show_anagrams"))  # anagrams=anagrams)


@app.route("/anagrams")
def show_anagrams():
    """Display anagrams."""
    return render_template("result.html")
