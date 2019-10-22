import sys


def go_to_next_line():
    """Helper function to make console go to next line, at the end of
       reverse() execution.
    """
    print("")


def decide_if_sentence(input):
    """Decide if the input is multiple word or many (making it a sentence)
       Param: input(list)
       Return: bool
    """
    return len(input) > 1


def reverse(input):
    """Returns the input string in reverse.
       Param: input(list): can be either a single word or multiple strings
    """
    # if input_str is a sentence, then outputs words in sentence in reverse
    if decide_if_sentence(input) is True:
        sentence = list()
        for word in input:
            sentence.append(word)

        # output reverse sentence
        sentence_length = len(sentence)
        for i in range(sentence_length):
            last_word_index = sentence_length - (i + 1)
            last_word = sentence[last_word_index]
            print(last_word, end=" ")

        go_to_next_line()

    # if input_str is a single word, then outputs letters in reverse
    else:
        word = list()
        for letter in input:
            word.append(letter)

        # output word in reverse
        word_length = len(word)
        for i in range(word_length):
            letter_from_end_index = i + 1
            letter_from_end = word[word_length - letter_from_end_index]
            print(letter_from_end, end="")

        go_to_next_line()


if __name__ == "__main__":
    reverse(sys.argv[1:])
