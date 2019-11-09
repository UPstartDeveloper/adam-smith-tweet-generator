from flask import Flask, render_template, redirect, url_for, request
from dictogram import Dictogram
from stochastic_sampling import stochastic_sample
from clean_words import get_clean_words
from markov_chain import MarkovChain

# Flask app for tweet generator
app = Flask(__name__)
# create a markov chain
fish_list = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
mark = MarkovChain(fish_list)


def get_words(num_words=10):
    """Capitalize the word letter of a string.
       Param: num_words (int): amount of words to put in sentence
       Return: words(list): str where first str is capitalized, 10 for sentence
    """
    # sentence tp be displayed
    words = mark.random_walk(num_words)
    # capitalize first letter of starting word
    first_letter = words[0].upper()
    words = first_letter + words[1:]
    return words


@app.route("/")
def index():
    '''Display a sentence on each reload.'''
    # generate 10 words on default for first load of page
    words = get_words()
    return render_template("index.html", words=words)


@app.route("/reload")
def reload():
    '''Redirect user to a new load of the home page.'''
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
