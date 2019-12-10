import sys
import re


def parse_word(word):
    '''Given a str, returns a str cleaned of undesirable symbols.'''
    word = word.replace('.', '')
    word = word.replace('?', '')
    word = word.replace('!', '')
    word = word.replace(',', '')
    word = word.replace(':', '')
    word = word.replace(';', '')
    word = word.replace('(', '')
    word = word.replace(')', '')
    word = word.replace('{', '')
    word = word.replace('}', '')
    return word


def get_clean_words():
    """Get a list of single-word strings from source text.
        Param: file_name(str)
        Return: clean_words_as_str(list)
    """
    words = []
    # collect words from .txt files
    with open("adam_smith.txt", "r") as file:
        words = file.read().split()
    with open("more_adam_smith.txt", "r") as file:
        words.extend(file.read().split())
    # remove all occurences of non-alpha chars from data
    clean_words = []
    for word in words:
        # clean words for punctuation, unwanted symbols
        clean_words.append(parse_word(word.lower()))
    # make a list of whole words only containing letters
    clean_words_as_str = []
    for list_of_chars in clean_words:
        whole_word = ""
        clean_words_as_str.append(whole_word.join(list_of_chars))

    return clean_words_as_str


if __name__ == "__main__":
    # file = "adam_smith.txt"
    print(len(get_clean_words()))
