import tweet_gen_app.stochastic_sampling as sampler_helper
import random


def calculate_length_of_source(listogram):
    """Return the total number of tokens in the histogram."""
    tokens = 0
    for list in histogram:
        tokens += list[1]
    return tokens


def fit_in_range(listogram, index, dart):
    """Decide if the word at this index in the listogram is associated with
       a range clearly containing the dart value.
       Param: listogram(Listogram)
              index(int)
              dart
       Return: True, or
               the index position (before or after) of the word to compare
               ranges with
    """
    # check if the dart clearly falls in the range at this index position
    range = listogram[index][1]
    low_end = range[0]
    high_end = range[1]
    if dart < high_end and dart > low_end:
        return True
    else:
        # check if the dart is between the range here and the range before
        index_before = index - 1
        range_before = listogram[index][1]
        if dart == range_before[1]:
            return index_before
        else:
            # check if the dart is between the range here and the range after
            index_after = index + 1
            range_after = listogram[index][1]
            if dart == range_before[0]:
                return index_after


def choose_word(listogram, dart):
    """Return the word in the listogram whose associated tuple contains the
       dart, such that list[0] <= dart <= list[1],
       where dart is a float number between 0 and 1 inclusive,
       and list is the tuple, located at the second index in each of the list
       elements in the overall listogram.
       Param: listogram(Listogram)
              dart(float)
       Return: word(str)
    """
    if dart == 0.0:
        return listogram[0][0]  # return the first word
    elif dart == 1.0:
        return listogram[-1][0]  # return the last word
    # find out which word associates to the range containing the dart, or if
    # the dart falls in between two words' ranges exactly
    else:
        for index in range(len(listogram)):
            # decide if the word at this index has the range containing dart
            word = listogram[index][0]
            if fit_in_range(listogram, index, dart) is True:
                return word
            else:
                # compare ranges of the two words dart falls between
                pass


def weighted_sample(listogram):
    """Chooses a random word from the histogram of word frequency.
       Words that have higher frequnecy counts in the histogram will
       be chosen more often by this function.
       Param: listogram(Listogram)
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
    # generate word, influence outcome using weighted probability
    dart = random.uniform(0, 1)
    word = choose_word(listogram, dart)
