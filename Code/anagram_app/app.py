from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


def get_words():
    """Get words from the words file to get anagrams from."""
    # get words from the words file
    file = open("/usr/share/dict/words", "r")
    words_list = file.readlines()
    file.close()
    # removing newline characters from strings in words file
    words_no_newline = list()
    for word in words_list:
        word = word[:-3]
        words_no_newline.append(word)
    return words_no_newline


@app.route("/")
def get_input():
    """Show form for user to input a string to make anagrams from (a word)."""
    return render_template("form.html")


@app.route("/word")
def parse_data():
    """Generates anagrams from the input string."""
    input = request.args.get("string")
    anagrams = list()
    words_to_choose_from = get_words()
    # determine which words are anagrams of the input
    for word in words_to_choose_from:
        for letter in input:
            if letter in word:
                if len(input) == len(word) and (not input == word):
                    anagrams.append(word)
    return redirect(url_for("show_anagrams", anagrams=anagrams))


@app.route("/anagrams/<anagrams>")
def show_anagrams(anagrams):
    """Display anagrams."""
    return render_template("result.html", anagrams=anagrams)
