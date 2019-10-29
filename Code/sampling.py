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
    low_end = probability
    high_end = probability + (factor * current_value)
    probability = high_end
    return tuple(low_end, high_end, probability)


def choose_bucket(histogram, dart):
    """Return the word that the dart lands on.
       Param: histogram(dict): a representation of the word frequency for a
              source text
              dart(float): a random number between 0 and 1
        Return: word(str): a type of word from the text
    """
    words = histogram.keys()
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
            range_of_word_after = calc_range(histogram, words, index_after)
            range_here = calc_range(histogram, words, i)
            # see which one is greater, or if equal just default to previous
            if range_here > range_of_word_after:
                return words[i]
            else:
                return words[index_after]


def sample(source_text):
    """Return a random word from a source text,
       weighted by frequency of the word.
       Param: source_text(str): file name for text being sampled from
       Return: (str)
    """
    histogram = histogram(sys.argv[1])


if __name__ == "__main__":
    print(sample(sys.argv[1]))
