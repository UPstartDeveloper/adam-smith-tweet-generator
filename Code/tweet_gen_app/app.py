from flask import Flask, render_template, redirect, url_for, request
from dictogram import Dictogram
from stochastic_sampling import stochastic_sample
from clean_words import get_clean_words
from markov_chain import MarkovChain
from pymongo import MongoClient
import os

# Flask app for tweet generator
app = Flask(__name__)
# create a markov chain
mark = MarkovChain()

# add Mongo database
host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Tweets')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
favorites = db.favorites


def get_words(num_words):
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


@app.route("/", methods=['GET', 'POST'])
def index():
    '''Display a sentence.'''
    # show 10 words on the first load
    num = request.form.get('num')
    if num == '' or num is None:
        num = 10
    words = get_words(int(num))
    return render_template("index.html", words=words)
    # user has inputted a number of words to generate
    if request.method == 'POST':
        # int_num_words = request.form.get('num')
        return redirect(url_for('index'))


@app.route("/new_favorite", methods=['POST'])
def add_to_favorites():
    """Add the sentence into the favorites database."""
    words = request.form['words']
    sentence = {
        'tweet_phrase': words
    }
    favorites.insert_one(sentence)
    return redirect(url_for('index'))


@app.route("/favorites")
def show_favorites():
    """List all Tweets marked as favorites by the users."""
    return render_template("favorites.html", favorites=favorites.find())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
