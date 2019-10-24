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


def create_histogram_list_of_lists(words_list):
    pass


def create_histogram_list_of_tuples(words_list):
    pass


def create_histogram_dict_inverted(words_list):
    pass


def histogram(file_name):
    """Return a histogram of the appearances of words from a .txt file.
       Param: file_name(str): name of file with source text (.txt)
       Return: histogram(dict): every key a unique word,
               and value is appearances
               of the word in the text
    """
    words_list = get_clean_words(file_name)
    # make a dict of the data
    histogram = create_histogram_dict(words_list)
    # histogram = create_histogram_list_of_lists(words_list)

    return histogram


def determine_hist_type(histogram):
    """Return the data type of the histogram.
       Param: histogram: dict, list of lists, or list of tuples
       Return: str
    """
    if isinstance(histogram, dict) is True:
        # determine if keys in dict are word strings or numbers
        words_or_num = list(histogram.keys())
        if isinstance(words_or_num[0], str) is True:
            return "dict_with_str_keys"
        else:
            return "dict_with_num_keys"
    elif isinstance(histogram, list) is True:
        # determine if histogram is made of lists or tuples
        if isinstance(histogram[0], list) is True:
            return "list_lists"
        elif isinstance(histogram[0], tuple) is True:
            return "list_tuples"


def unique_words(histogram):
    """Return total count of unique words in a source text.
       Param: histogram(dict, list of lists, or list of tuples)
       Return: int
    """
    if determine_hist_type(histogram) == "dict_with_str_keys":
        return len(list(histogram.keys()))
    elif determine_hist_type(histogram) == "dict_with_num_keys":
        pass
    elif determine_hist_type(histogram) == "list_lists":
        pass
    elif determine_hist_type(histogram) == "list_tuples":
        pass


def frequency(word, histogram):
    '''Returns the frequency of a word in a text.
       Param: word(str): word being analyzed
              histogram(dict, list of lists or tuples): represents source text
       Returns: int
    '''
    if determine_hist_type(histogram) == "dict_with_str_keys":
        return histogram[word]
    elif determine_hist_type(histogram) == "dict_with_num_keys":
        pass
    elif determine_hist_type(histogram) == "list_lists":
        pass
    elif determine_hist_type(histogram) == "list_tuples":
        pass


if __name__ == "__main__":
    # print(histogram(sys.argv[1]))
    # print(unique_words(histogram(sys.argv[1])))
    print(frequency('newsletter', histogram(sys.argv[1])))
