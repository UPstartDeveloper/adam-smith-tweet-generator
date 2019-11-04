import random
import sys


def get_words_list():
    """Return a list of words from words file, with no newline characters."""
    # get words from the file
    lines = list()
    with open("/usr/share/dict/words", "r") as file:
        lines = file.readlines()
    # removing newline characters from strings in words file
    words_no_newline = [line.strip() for line in lines]

    return words_no_newline


def make_sentence(words_list, num_words):
    """Get the number of words requested by user randomly.
       Params:
       words_list(list): list of str to choose words from randomly
       num_words(int)
       Returns:
       sentence(list)
    """
    sentence = list()
    for i in range(num_words):
        random_index = random.randrange(len(words_list) - 1)
        sentence.append(words_list[random_index])
    return sentence


def print_sentence(sentence):
    """Displays words in terminal.
       Param: sentence(list of str)
    """
    for word in sentence:
        print(word, end=" ")
    # move to next line in terminal
    print("")


def random_words_from_dictionary(num_requested):
    """
        Return a sentence of words randomly chosen from a file.
        Param: num_requested(int): number of words in sentence
    """
    words = get_words_list()
    sentence = make_sentence(words, num_requested)
    print_sentence(sentence)


if __name__ == "__main__":
    num = int(sys.argv[1])
    random_words_from_dictionary(num)
