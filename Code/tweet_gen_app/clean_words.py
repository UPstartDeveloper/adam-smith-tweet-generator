import sys
import re


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
        clean_word = ([char for char in word.lower() if not (
            char == "." or
            char == "?" or
            char == "!" or
            char == "," or
            char == ":" or
            char == ";" or
            char == "(" or
            char == ")"
        )])
        clean_words.append(clean_word)
    # make a list of whole words only containing letters
    clean_words_as_str = []
    for list_of_chars in clean_words:
        whole_word = ""
        clean_words_as_str.append(whole_word.join(list_of_chars))

    return clean_words_as_str


if __name__ == "__main__":
    file = "adam_smith.txt"
    print(len(get_clean_words()))
