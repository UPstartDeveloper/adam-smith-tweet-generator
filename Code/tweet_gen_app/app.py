from flask import Flask, render_template, redirect, url_for, request
from dictogram import Dictogram
from stochastic_sampling import stochastic_sample
from clean_words import get_clean_words
from markov_chain import MarkovChain

# Flask app for tweet generator
app = Flask(__name__)
# create a markov chain
mark = MarkovChain()


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
    '''Display a sentence on the first load.'''
    # Generates 10 words on default for first load of page
    words = get_words()
    return render_template("index.html", words=words)


@app.route("/<num>", methods=['GET'])
def reload(num):
    '''Display a sentence on each reload.'''
    num = request.form.get('num')
    num_words = int(num)
    words_list = get_words(num)
    return render_template("index.html", words=words_list)


if __name__ == "__main__":
    app.run(debug=True)
