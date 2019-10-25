import sys
import re


def get_clean_words(file_name):
    """Get a list of single-word strings from source text.
        Param: file_name(str)
        Return: words(list)
    """
    words = []
    with open(file_name, "r") as file:
        # make a list ofd words, contains non alphabetic chars
        words = file.read().split()
        # remove all occurences of non-alpha chars from data
        clean_words = []
        for word in words:
            clean_word = ([char for char in word if not (
                char == "." or
                char == "?" or
                char == "!" or
                char == "," or
                char == ":" or
                char == ";" or
                char == "(" or
                char == ")"
            )])
            clean_words.append(clean_word)
        # make a list of whole words only containing letters
        clean_words_as_str = []
        for list_of_chars in clean_words:
            whole_word = ""
            clean_words_as_str.append(whole_word.join(list_of_chars))

    return clean_words_as_str


def create_histogram_dict(words_list):
    """Return a dictionary representing a histogram of words in a list.
       Param: words_list(list): list of strings representing words
       Return: histogram(dict): each key a unique word, values are number of
               word appearances
    """
    histogram = dict()
    words = histogram.keys()
    for word in words_list:
        if word.lower() not in words:
            histogram[word.lower()] = 1
        else:
            histogram[word.lower()] += 1
    return histogram


def find_unique_words(words_list):
    """Record all unique words in a list of strings."""
    # record all unique words
    unique_words = list()
    for word in words_list:
        if word.lower() not in unique_words:
            unique_words.append(word.lower())
    return unique_words


def create_histogram_list_of_lists(words_list):
    """Return a list to represent a histogram of word frequency in a text.
       List contains a list for each unique word in the text.
       First element in the nested list is the word; and the second element is
       the number of appearances that word makes in the text.
       Param: words_list(list): list of strings representing the text
       Return: histogram(list)
    """
    histogram = list()
    unique_words = find_unique_words(words_list)
    # generate histogram
    for word in words_list:
        # if word not recorded, make a new list for it in histogram
        if word.lower() not in unique_words:
            histogram.append([word.lower(), 1])
            unique_words.append(word.lower())
        # find the list containing non-unique words, and increment appearances
        else:
            word_index = unique_words.index(word.lower())
            histogram[word_index][1] += 1
    return histogram


def create_histogram_list_of_tuples(words_list):
    """Return the equivalent of the previous function, using tuples (instead of
       lists) nested inside a list.
    """
    histogram = list()
    unique_words = find_unique_words(words_list)
    # count up appearances of each unique word, then make tuple in histogram
    for word in unique_words:
        appearances = 0
        for word_from_text in words_list:
            if word == word_from_text.lower():
                appearances += 1
        histogram.append((word, appearances))

    return histogram


class Word:
    def __init__(self, word, appearances=0):
        self.word = word
        self.appearances = appearances


def create_histogram_inverted(words_list):
    """Create a histogram of word frequency from a source text.
       Each tuple's first element is a number representing the
       appearances of a word.
       Each value is a list of words which appear that number of times.
       Param: words_list(list)
       Return: histogram(list): contains nested tuples with nested lists
    """
    unique_words = find_unique_words(words_list)
    unique_words_as_obj = [Word(word) for word in unique_words]
    # count up appearances for each Word
    for word in unique_words_as_obj:
        for word_from_text in words_list:
            if word.word == word_from_text:
                word.appearances += 1
    # make a histogram by grouping Word objects with equal appearances together
    histogram = list()
    count_of_appearances = 0
    while len(histogram) < len(unique_words_as_obj):
        for word in unique_words_as_obj:
            count_of_appearances += 1
            words_having_appearances = list()
            word_count = (count_of_appearances, words_having_appearances)
            if word.appearances == count_of_appearances:
                words_having_appearances.append(word.word)
        histogram.append(word_count)

    return histogram
    """
    histogram = list()
    unique_words = find_unique_words(words_list)
    count_of_appearances = 0
    for word in unique_words:
        count_of_appearances += 1
        appearances = 0
        words_having_appearances = list()
        for i in range(len(words_list)):
            if word == word_list[i].lower():
                appearances += 1
        if count_of_appearances == appearances:
            words_having_appearances.append(word)
    """


def histogram(file_name):
    """Return a histogram of the appearances of words from a .txt file.
       Param: file_name(str): name of file with source text (.txt)
       Return: histogram(dict): every key a unique word,
               and value is appearances
               of the word in the text
    """
    words_list = get_clean_words(file_name)
    # make a dict of the data
    # histogram = create_histogram_dict(words_list)
    histogram = create_histogram_list_of_lists(words_list)
    # histogram = create_histogram_list_of_tuples(words_list)
    # histogram = create_histogram_inverted(words_list)

    return histogram


def determine_hist_type(histogram):
    """Return the data type of the histogram.
       Param: histogram: dict, list of lists, or list of tuples
       Return: str
    """
    if isinstance(histogram, dict) is True:
        # determine if keys in dict are word strings or numbers
        return "dict"
    elif isinstance(histogram, list) is True:
        # determine if histogram is inverted or not
        if isinstance(histogram[0], str) is True:
            return "list"
        else:
            return "inverted_list"


def unique_words(histogram):
    """Return total count of unique words in a source text.
       Param: histogram(dict, list of lists, or list of tuples)
       Return: int
    """
    if determine_hist_type(histogram) == "dict":
        return len(list(histogram.keys()))
    elif determine_hist_type(histogram) == "list":
        return len(histogram)
    elif determine_hist_type(histogram) == "inverted_list":
        count_of_words = 0
        for tuple in histogram:
            count_of_words += len(tuple[1])
        return count_of_words


def frequency(word, histogram):
    '''Returns the frequency of a word in a text.
       Param: word(str): word being analyzed
              histogram(dict, list of lists or tuples): represents source text
       Returns: int
    '''
    if determine_hist_type(histogram) == "dict":
        return histogram[word]
    elif determine_hist_type(histogram) == "list":
        for i in range(len(histogram)):
            if histogram[i] == word:
                return histogram[i][1]
    elif determine_hist_type(histogram) == "inverted_list":
        for tuple in histogram:
            if word in tuple[1]:
                return tuple[0]


def most_least_frequent(histogram):
    """Return a tuple of the most and least frequent
        words in a histogram.
    """
    # implement for a histogram that uses list of lists
    if determine_hist_type(histogram) == "list":
        # find the most frequent word
        appearances = 0
        most_frequent_word = ""
        for list in histogram:
            if list[1] > appearances:
                appearances = list[1]
                most_frequent_word = list[0]
        # find the least frequent word
        least_frequent_word = ""
        for list in histogram:
            if list[1] < appearances:
                appearances = list[1]
                least_frequent_word = list[0]
        return (most_frequent_word, least_frequent_word)


if __name__ == "__main__":
    # print(histogram(sys.argv[1]))
    # print(unique_words(histogram(sys.argv[1])))
    # print(frequency('newsletter', histogram(sys.argv[1])))
    with open(sys.argv[1]) as file:
        if file.name == "adam_smith.txt":
            print("Analysis of THE WEALTH OF NATIONS (1776), by Adam Smith")
