import tweet_gen_app.stochastic_sampling as sampler_helper
import random


def calculate_length_of_source(histogram):
    """Return the total number of tokens in the histogram."""
    tokens = 0
    for list in histogram:
        tokens += list[1]
    return tokens


def weighted_sample(histogram):
    """Chooses a random word from the histogram of word frequency.
       Words that have higher frequnecy counts in the histogram will
       be chosen more often by this function.
       Param: histogram(list of lists)
       Return: word(str)
    """
    # set up needed values
    length_of_text = calculate_length_of_source(histogram)
