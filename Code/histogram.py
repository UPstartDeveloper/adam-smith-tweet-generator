from clean_words import get_clean_words


def create_histogram_dict(words_list):
    """Return a dictionary representing a histogram of words in a list.

       Parameters:
       words_list(list): list of strings representing words

       Returns:
       histogram(dict): each key a unique word, values are number of
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
    '''Record all unique words in a list of strings.'''
    # record all unique words
    unique_words = list()
    for word in words_list:
        if word.lower() not in unique_words:
            unique_words.append(word.lower())
    return unique_words


def make_word_appearance_pairs(words_list):
    '''Return a list of word and the number of appearances they make in a list.'''
    histogram = list()
    unique_words = find_unique_words(words_list)
    # count up appearances of each unique word, then make tuple in histogram
    for word in unique_words:
        appearances = 0
        for word_from_text in words_list:
            if word == word_from_text.lower():
                appearances += 1
        histogram.append([word, appearances])

    return histogram


def create_histogram_list_of_lists(words_list):
    """Return a list to represent a histogram of word frequency in a text.
       List contains a list for each unique word in the text.
       First element in the nested list is the word; and the second element is
       the number of appearances that word makes in the text.

       Parameters:
       words_list(list): list of strings representing the text

       Returns:
       histogram(list)

    """
    return make_word_appearance_pairs(words_list)


def create_histogram_list_of_tuples(words_list):
    '''Return a histogram stuctured as a list of nested tuples.'''
    histogram = make_word_appearance_pairs(words_list)
    # make each nested list a tuple
    histogram = [tuple(list) for list in histogram]
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

       Parameters:
       words_list(list)

       Returns:
       histogram(list): contains nested tuples with nested lists

    """
    unique_words = find_unique_words(words_list)
    unique_words_as_obj = [Word(word) for word in unique_words]
    # count up appearances for each Word
    for word in unique_words_as_obj:
        for word_from_text in words_list:
            if word.word == word_from_text.lower():
                word.appearances += 1
    # make a histogram by grouping Word objects with equal appearances together
    histogram = list()
    count_of_appearances = 0
    # while len(histogram) < len(unique_words_as_obj):
    for word in unique_words_as_obj:
        count_of_appearances += 1
        words_having_appearances = list()
        word_count = (count_of_appearances, words_having_appearances)
        if word.appearances == count_of_appearances:
            words_having_appearances.append(word.word)
            histogram.append(word_count)

    return histogram


def histogram():
    """Return a histogram of the appearances of words from a .txt file.

       Parameters:
       None

       Returns:
       histogram(dict): every key a unique word, and value is appearances
                        of the word in the text

    """
    words_list = get_clean_words()
    # make a dict of the data
    histogram = create_histogram_dict(words_list)
    # histogram = create_histogram_list_of_lists(words_list)
    # histogram = create_histogram_list_of_tuples(words_list)
    # histogram = create_histogram_inverted(words_list)

    return histogram


def determine_hist_type(histogram):
    """Return the data type of the histogram.

       Parameters:
       histogram(dict or list): dict, list of lists, or list of tuples

       Returns:
       str: declares what the object type of the histogram is

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

       Parameters:
       histogram(dict, list of lists, or list of tuples): an object
       used to observe word frequency from a source text

       Returns:
       int: number of word types in the histogram

    """
    if determine_hist_type(histogram) == "dict":
        return len(list(histogram.keys()))
    elif determine_hist_type(histogram) == "list":
        return len(histogram)
    elif determine_hist_type(histogram) == "inverted_list":
        count_of_words = 0
        for tuple in histogram:
            count_of_words += tuple[1]
        return count_of_words


def frequency(word, histogram):
    """Returns the frequency of a word in a text.

       Parameters:
       word(str): word being analyzed
       histogram(dict, list of lists or tuples): represents source text

       Returns:
       int: number of tokens for the given word type

    """
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
    '''Return a tuple of the most and least frequent words in a histogram.'''
    # implement for a histogram that uses list of lists
    if determine_hist_type(histogram) == "list":
        # find the most frequent word
        frequency_to_beat = 0
        most_frequent_word = ""
        for list in histogram:
            word = list[0]
            frequency = frequency(word, histogram)
            if frequency > frequency_to_beat:
                most_frequent_word = word
                frequency_to_beat = frequency
        # find the least frequent word
        least_frequent_word = ""
        for list in histogram:
            word = list[0]
            frequency = frequency(word, histogram)
            if frequency < frequency_to_beat:
                least_frequent_word = word
                frequency_to_beat = frequency
        return tuple(most_frequent_word, least_frequent_word)


def total_count(histogram):
    '''Return total number of words in a text given a histogram.'''
    total_count = 0
    for pairing in histogram:
        total_count += pairing[1]
    return total_count


def calculate_mean(histogram):
    """Return the mean number of appearances for word frequency.
       Divide total lword count of text by the number of unique words.

       Parameters:
       histogram(list or dict)

       Return:
       float: mean number of appearances across all word types

    """
    if determine_hist_type(histogram) == "list":
        total_count = total_count(histogram)

        return (float(total_count)/len(histogram))


def calculate_median(histogram):
    '''Return the median word frequency from a histogram.'''
    if determine_hist_type(histogram) == "list":
        # check whether length of text is even/odd
        total_count = total_count(histogram)
        length = len(histogram)
        if total_count % 2 == 0:
            sum = histogram[length / 2][1] + histogram[(length / 2) - 1][1]
            return (sum / 2)
        else:
            # return the appearances of the index position that's
            # half the length of the histogram minus
            return histogram[(length - 1) / 2][1]


def calculate_mode(histogram):
    '''Return the number of appearances made by the most frequent word.'''
    most_frequent_word = most_least_frequent(histogram)[0]
    return frequency(most_frequent_word, histogram)


if __name__ == "__main__":
    # print(histogram(sys.argv[1]))
    # print(unique_words(histogram(sys.argv[1])))
    # print(frequency('newsletter', histogram(sys.argv[1])))
    histogram = histogram()
    '''
    most_least_frequent = most_least_frequent(histogram)
    unique_words = unique_words(histogram)
    print("Analysis for THE WEALTH OF NATIONS (1776), by Adam Smith:")

    # get stats on the source text
    (most, least) = most_least_frequent(histogram)
    print(f"Most frequent word: {most}")
    print(f"Least frequent word: {least}")

    word_amt = unique_words(histogram)
    print(f"Number of words used: {word_amt}.")

    mean = calculate_mean(histogram)
    print(f"Mean word frequency: {mean}.")

    median = calculate_median(histogram)
    print(f"Median word frequency: {median}.")

    mode = calculate_mode(histogram)
    print(f"Mode word frequency: {mode}.")
    '''
