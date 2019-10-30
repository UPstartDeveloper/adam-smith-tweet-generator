from flask import Flask
# Flask app for tweet generator

app = Flask(__name__)


@app.route("/")
def index():
    """Display a single generated word on each reload."""
    return "Hello, World!"  # welcome message to start


if __name__ == "__main__":
    app.run(debug=True)
