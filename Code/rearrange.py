import sys
import random


def rearrange(words):
    """Prints every str in a list, in a randomly rearranged order.
        Param: words (list of str object)
        Return: None
    """
    # create a list storing str from words in a randomly decided order
    rearranged_words = list()
    while not len(words) == 0:
        rand_index = random.randint(0, len(words) - 1)
        random_word = words[rand_index]
        if random_word not in rearranged_words or len(words) > 0:
            rearranged_words.append(random_word)
            words.remove(random_word)

    # show the order of str in rearranged_words
    for word in rearranged_words:
        print(word, end=" ")
    # go to a new to make console output cleaner
    print("")


if __name__ == "__main__":
    words = sys.argv[1:]
    rearrange(words)
