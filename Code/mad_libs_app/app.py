from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


@app.route("/")
def show_form():
    """Present a from for user to input words for the Mad Libs story."""
    return "Hello user!"


if __name__ == "__main__":
    app.run(debug=True)
