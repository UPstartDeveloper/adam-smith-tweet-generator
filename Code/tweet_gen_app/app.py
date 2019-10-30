from flask import Flask, render_template
import sys
sys.path.append('../')
from histogram import histogram
from stochastic_sampling import stochastic_sample


# importing corpus text and creating a histogram
corpus = "../adam_smith.txt"
histo = histogram(corpus)
# Flask app for tweet generator
app = Flask(__name__)


@app.route("/")
def index():
    """Display a single generated word on each reload."""
    word = stochastic_sample(histo)
    return render_template("index.html", word=word)


if __name__ == "__main__":
    app.run(debug=True)
