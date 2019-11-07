import tweet_gen_app.stochastic_sampling as sampler_helper
import random


def calculate_length_of_source(listogram):
    """Return the total number of tokens in the histogram."""
    tokens = 0
    for list in histogram:
        tokens += list[1]
    return tokens


def weighted_sample(listogram):
    """Chooses a random word from the histogram of word frequency.
       Words that have higher frequnecy counts in the histogram will
       be chosen more often by this function.
       Param: listogram(list of lists)
       Return: word(str)
    """
    # set up needed values
    length_of_text = calculate_length_of_source(listogram)
    probability_factor = sampler_helper.calculate_factor(length_of_text)
    probability = 0
    # reassign word counts in listogram to ranges of values that dart can equal
    for list in listogram:
        current_value = list[1]
        current_value = sampler_helper.make_range(probability,
                                                  probability_factor,
                                                  current_value)
        probability = current_value[1]
    print(listogram)
