import tweet_gen_app.stochastic_sampling as sampler_helper
import random


def calculate_length_of_source(listogram):
    """Return the total number of tokens in the histogram."""
    tokens = 0
    for list in listogram:
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
    if dart > low_end and dart < high_end:
        return True
    else:
        # check if the dart is between the range here and the range before
        if dart == listogram[index][1][0]:
            index_before = index - 1
            return index_before
        else:
            # check if the dart is between the range here and the range after
            if dart == listogram[index][1][1]:
                index_after = index + 1
                return index_after
            else:
                # if the dart is nowhere near this range
                return False


def find_size_of_range(low_end, high_end):
    """Return size of the range."""
    return high_end - low_end


def store_range_size(listogram, index, list_of_sizes):
    """Store the difference between the high end and low end of the range
       associated with a word in a list.
       Param: listogram(Listogram),
              index(int),
              list_of_sizes(list)
       Return: modified list_of_sizes
    """
    low_end = listogram[index][1][0]
    high_end = listogram[index][1][1]
    size_of_range_of_word = find_size_of_range(low_end, high_end)
    list_of_sizes.append(size_of_range_of_word)
    return list_of_sizes


def compare_ranges(listogram, index, other_index):
    """Determine which word has the larger range which dart falls within.
       If they are of equal size, then the word associated with index returns.
       Param: listogram(Listogram),
              index(int),
              other_index(int)
       Return: word(str)
    """
    range_sizes = list()  # stores the difference between the low and high ends
    # store the range sizes of both of the words
    range_sizes = store_range_size(listogram, index, range_sizes)
    range_sizes = store_range_size(listogram, other_index, range_sizes)
    # make the choice, find the word which belongs with the choice
    word = listogram[index][0]
    other_word = listogram[other_index][0]
    if range_sizes[0] < range_sizes[1]:
        return other_word
    else:
        return word


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
            does_fit = fit_in_range(listogram, index, dart)
            if does_fit is not False:
                if does_fit is True:
                    return word
                else:
                    # compare ranges of the two words dart falls between
                    index_of_other_word = does_fit
                    word = compare_ranges(listogram, index, index_of_other_word)
                    return word


def restore_frequencies(listogram, factor):
    """Reassigns all values in the histogram dictionary back to their original
       counts.
       Param: listogram(Listogram): all values are now tuples
              factor(float): equal to 1/number of word tokens
       Return:listogram
    """
    for list in listogram:
        high_end_of_range = list[1][1]
        low_end_of_range = list[1][0]
        difference = high_end_of_range - low_end_of_range
        list[1] = round(difference / factor)
    return listogram


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
        list[1] = sampler_helper.make_range(probability,
                                            probability_factor,
                                            current_value)
        high_end = list[1][1]
        probability = high_end
    # generate word, influence outcome using weighted probability
    dart = random.uniform(0, 1)
    word = choose_word(listogram, dart)
    # restore frequency counts in the listogram here, then return the word
    listogram = restore_frequencies(listogram, probability_factor)
    return word
