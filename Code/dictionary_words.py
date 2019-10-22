import random
import sys


def random_words_from_dictionary(num_requested):
    """
        Return a sentence of words randomly chosen from a file.
        Param: num_requested(int): number of words in sentence
    """
    # get words from the words file
    file = open("/usr/share/dict/words", "r")
    words_list = file.readlines()
    file.close()
    # removing newline characters from strings in words file
    words_no_newline = list()
    for word in words_list:
        word = word[:-3]
        words_no_newline.append(word)
    # taking a portion from all the words to make a sentence from
    sentence = random.sample(words_no_newline, num_requested)

    # print out words in the sentence, then move on to next line in console
    for word in sentence:
        print(word, end=" ")
    print("")


if __name__ == "__main__":
    num = int(sys.argv[1])
    random_words_from_dictionary(num)
