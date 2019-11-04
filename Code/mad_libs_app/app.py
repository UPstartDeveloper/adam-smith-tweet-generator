from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


@app.route("/")
def show_form():
    """Present a from for user to input words for the Mad Libs story."""
    return render_template("index.html")


@app.route("/story", methods=["POST"])
def make_story():
    """Make Mad Libs story from user input."""
    noun = request.form.get("noun")
    verb = request.form.get("verb")
    adj = request.form.get("adjective")

    story = f"{noun}"

    return redirect(url_for("display_story", story=story))


if __name__ == "__main__":
    app.run(debug=True)
