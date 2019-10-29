from histogram import create_histogram_dict, histogram, get_clean_words
import sys
import random


def calculate_length_of_source(histogram):
    """Return the total count of words in the source text.
       Param: histogram(dict)
       Return: int
    """
    sum = 0
    words = histogram.keys()
    for word in words:
        sum += histogram[word]
    return sum


def calculate_factor(length):
    """Return the fraction of the source text for a single token.
       Param: length(int): the total number of words in the text
       Return: (float) the inverse of the length
    """
    return (float(1)/length)


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
    pass


def choose_bucket(histogram, dart):
    """Return the word that the dart is most likely to land on.
       Param: histogram(dict): a representation of the word frequency for a
              source text
              dart(float): a random number between 0 and 1
        Return: word(str): a type of word from the text
    """
    pass


def sample(source_text):
    """Return a random word from a source text,
       weighted by frequency of the word.
       Param: source_text(str): file name for text being sampled from
       Return: (str)
    """
    histogram = histogram(sys.argv[1])


if __name__ == "__main__":
    print(sample(sys.argv[1]))
