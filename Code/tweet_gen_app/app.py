from flask import Flask, render_template, redirect, url_for, request
from dictogram import Dictogram
from stochastic_sampling import stochastic_sample
from clean_words import get_clean_words

# Flask app for tweet generator
app = Flask(__name__)


def get_words():
    """Capitalize the word letter of a string.
       Param: none
       Return: words(list): str where first str is capitalized, 10 for sentence
    """
    # creating a histogram
    words_list = get_clean_words("adam_smith.txt")
    histo = Dictogram(words_list)
    # making a list to store words
    words = list()
    for i in range(10):
        words.append(stochastic_sample(histo))
    # capitalize first letter of starting word
    first_word = words[0]
    first_letter = first_word[0].upper()
    rest_of_word = first_word[1:]
    reassigned_word = first_letter + rest_of_word
    words[0] = reassigned_word
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
