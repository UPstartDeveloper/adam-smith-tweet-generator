import histogram
import sys
import random
from sampling import random_word


def calculate_length_of_source(histogram):
    """Return the total count of words in the source text.
       Param: histogram(dict)
       Return: int
    """
    sum = 0
    for word in list(histogram):
        sum += histogram[word]
    return sum


def calculate_factor(length):
    """Return the fraction of the source text for a single token.
       Param: length(int): the total number of words in the text
       Return: (float) the inverse of the length
    """
    return (1.0/float(length))


def make_range(probability, factor, current_value):
    """Return a tuple to be the new value in the histogram dictionary.
       Param: probability (float): num in the sample spacee currently
              factor (float): the fraction of the source text for a token
              current_value(int): appearances of a type of word in text
       Return: (tuple) of 3 elements:
                1. lower end of the sample space a word comprises
                2. higher end of the sample space a word comprises
                3. new value to update probability to
    """
    low_end = probability
    high_end = probability + (factor * current_value)
    probability = high_end
    return tuple((low_end, high_end, probability))


def calculate_range(histogram, words, index):
    """Return the difference between the high and low ends of a range for a
       value in the modified histogram.
       Param: histogram(dict): modified so each value is a tuple
              words(list): a list of the keys in histogram
              index(int): a way for us to access the value in the histogram
       Return: (float)
    """
    return (histogram[words[index]][1] - histogram[words[index]][0])


def choose_bucket(histogram, dart):
    """Return the word that the dart lands on.
       Param: histogram(dict): a representation of the word frequency for a
              source text
              dart(float): a random number between 0 and 1
        Return: word(str): a type of word from the text
    """
    words = list(histogram.keys())
    # decide which word the dart lands in, and choose between two if necessary
    for i in range(len(words)):
        if dart == 1.0:
            # return the last word
            return histogram[words[len(words) - 1]]
        elif dart == 0.0:
            # return the first word
            return histogram[words[0]]
        elif dart > histogram[words[i]][0] or dart < histogram[words[i]][1]:
            # dart clearly falls within the range of one word
            return words[i]
        elif dart == histogram[words[i]][0]:
            # compare this word's range of values with the previous
            index_before = i - 1
            # make ranges to compare
            range_of_prev = calc_range(histogram, words, index_before)
            range_here = calc_range(histogram, words, i)
            # see which one is greater, or if equal just default to previous
            if range_here > range_of_prev:
                return words[i]
            else:
                return words[index_before]
        elif dart == histogram[words[i]][1]:
            # # compare this word's range of values with the following
            index_after = i + 1
            # make ranges to compare
            range_of_word_after = calculate_range(histogram,
                                                  words, index_after)
            range_here = calculate_range(histogram, words, i)
            # see which one is greater, or if equal just default to previous
            if range_here > range_of_word_after:
                return words[i]
            else:
                return words[index_after]


def restore_frequencies(histogram, factor):
    """Reassigns all values in the histogram dictionary back to their original
       counts.
       Param: histogram(dict): all values are now tuples
              factor(float): equal to 1/number of distinct types of words
       Return: histogram(dict): all values are back to int
    """
    for word in histogram.keys():
        high_end_of_range = histogram[word][1]
        low_end_of_range = histogram[word][0]
        difference = high_end_of_range - low_end_of_range
        histogram[word] = (difference / factor)
    return histogram


def stochastic_sample(histo):
    """Return a random word from a source text,
       weighted by frequency of the word.
       Param: histo(dict): repredsents word frequency in the source_text
       Return: (str)
    """
    # set up needed values
    length_of_text = calculate_length_of_source(histo)
    probability_factor = calculate_factor(length_of_text)
    probability = 0
    # reassing values in histogram to tuples
    words = list(histo)
    for word in words:
        histo[word] = make_range(probability,
                                 probability_factor,
                                 histo[word])[0:2]
        probability = make_range(probability,
                                 probability_factor,
                                 probability)[2]
    # generate a word, influence outcome using each word's sample space
    dart = random.random()
    word = choose_bucket(histo, dart)
    # reassign values in histo to original value
    histo = restore_frequencies(histo, probability_factor)
    return word


# test functions start here
def words_in_text(histogram):
    """Return all unique_words in a source text,
       using the keys in the histogram.
       Param: histogrma(dict)
       Return: list
    """
    return list(histogram)


def make_sampling_histogram(unique_words):
    """Given a list of words, return a dictionary representing a histogram.
       All values begin at zero.
       Param: unique_words(list): every distinct type of word, will be a key
       Return: histogram_empty(dict)
    """
    histogram_empty = dict()
    for word in unique_words:
        histogram_empty[word] = 0
    return histogram_empty


def run_iterations(histogram_for_random_words, histogram_for_text):
    """Store the results of running the stochastic_sample function for 10,000
       iterations in a histogram.
       Param: histogram_for_random_words(dict): all values sum to a total of 0
              histogram_for_text(dict): all values represent frequency in text
       Return: histogram_for_random_words(dict): sum of all values = 10,000
    """
    unique_words = words_in_text(histogram_for_random_words)
    for i in range(10000):
        word = stochastic_sample(histogram_for_text)
        for key_word in unique_words:
            if word == key_word:
                histogram_for_random_words[word] += 1
    return histogram_for_random_words


def print_sampling_results(histogram_for_sampling):
    """Print all key value pairs in histogram_for_sampling.
       Param: histogram_for_sampling(dict)
       Return: None
    """
    unique_words = words_in_text(histogram_for_sampling)
    print("Results of Stochastic Sampling:")
    for word in unique_words:
        frequency = histogram_for_sampling[word]
        print(f"{word}: {frequency}")


def test_stochastic_sample(histogram_for_text):
    """Construct a histogram to represent the frequency of words being
       chosen by stochastic_sample. TEST function for stochastic_sample
       Param: histogram_for_text(dict)
       Return: None
    """
    histogram_for_sampling = dict()
    unique_words = words_in_text(histogram_for_text)
    # new histogram represents frequencies of words chosen by stochastic_sample
    histogram_for_sampling = make_sampling_histogram(unique_words)
    # run stochastic_sample 10K times, keep track of chosen words
    histogram_for_sampling = run_iterations(histogram_for_sampling,
                                            histogram_for_text)
    # print results
    print_sampling_results(histogram_for_sampling)


if __name__ == "__main__":
    # test samling with UNIFORM DISTRIBUTION
    text = sys.argv[1]
    hist = histogram.histogram(text)
    # word_no_weighting = random_word(hist)
    # print(f"Equally distributed: {word_no_weighting}")

    # random word sampled using frequency weighting
    # word_weighted = stochastic_sample(text)
    # print(f"Stochastically sampled: {word_weighted}")

    # show results of stochastic_sample
    test_stochastic_sample(hist)
