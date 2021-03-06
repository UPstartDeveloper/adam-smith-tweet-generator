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


def determine_anagram(word, possible_anagram):
    """Determines if a word might be the anagram of another word.
       Params:
       word(str)
       possible_anagram(str)
       Return bool
    """
    # possible_anagram cannot be a anagram if it isn't the same length as word
    if not len(word) == len(possible_anagram):
        return False
    # possible_anagram must be different from word
    elif word == possible_anagram:
        return False
    # possible_anagram must have all same letters as word
    for letter in possible_anagram:
        if letter not in word:
            return False

    for letter in word:
        if letter not in possible_anagram:
            return False
    # all tests passed, then return True
    return True


def remove_non_alpha(anagrams):
    '''Remove chars such as [, ', ], and commas that appear in the list of
       anagram strings.
       Param: anagrams(list)
       Return: clean(list)
    '''
    clean = list()
    for str in anagrams:
        word = ""
        if str.isalpha():
            word += str
        elif str == " " or str == "]":
            clean.append(word)


@app.route("/")
def get_input():
    """Show form for user to input a string to make anagrams from (a word)."""
    return render_template("form.html")


@app.route("/word", methods=["POST"])
def parse_data():
    """Generates anagrams from the input string."""
    input = request.form.get("string")
    anagrams = list()
    words_to_choose_from = get_words()
    # determine 10 words that are anagrams of the input
    for word in words_to_choose_from:
        if determine_anagram(input, word) is True:
            anagrams.append(word)
    return redirect(url_for("show_anagrams", anagrams=anagrams))


@app.route("/anagrams/<anagrams>")
def show_anagrams(anagrams):
    """Display anagrams."""
    # rememeber: anagrams is a string at this point
    # remove duplicates
    # anagrams = list(set(anagrams))
    return render_template("result.html", anagrams=anagrams)


if __name__ == "__main__":
    app.run(debug=True)
