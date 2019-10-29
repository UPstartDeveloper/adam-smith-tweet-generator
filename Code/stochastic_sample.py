import histogram
import sys
import random
# page 4 of the tutorial


def random_word(histogram):
    """Returns a random word from a histogram, which represents word frequency
       for a source text.
       Param: histogram(dict)
       Return: word(str)
    """
    word = ""
    words = list(histogram.keys())
    random_index = random.randint(0, len(words) - 1)
    word = words[random_index]
    return word


if __name__ == "__main__":
    histogram = histogram.histogram(sys.argv[1])
    print(random_word(histogram))
