import sys


def get_clean_words(file_name):
    """Get a list of single-word strings from source text.
        Param: file_name(str)
        Return: words(list)
    """
    words = []
    with open(file_name, "r") as file:
        list_of_lines = [line.strip("\n") for line in file.readlines()]
        lists_of_words = [line.split(" ") for line in list_of_lines]
        # add all word strings together in one big list
        all_words = []
        for list in lists_of_words:
            for str in list:
                if not (str == ""):
                    all_words.append(str)
    words = all_words
    return words


def histogram_as_dict(file_name):
    """Return a histogram of the appearances of words from a .txt file.
       Param: file_name(str): name of file with source text (.txt)
       Return: histogram(dict): every key a unique word,
               and value is appearances
               of the word in the text
    """
    words_list = get_clean_words(file_name)
    # make a dict of the data
    histogram = dict()
    words = histogram.keys()
    for word in words_list:
        if word not in words:
            histogram[word] = 1
        else:
            histogram[word] += 1

    return histogram

    """
    words_list = []
    with open(file_name, "r") as file:
        # words_list = [line.split(",") for line in file.readlines()]
        for line in file:
            for word in line:
                words_list.append(word)
    # words_list = remove_newlines(words_list)
    # print(words)
    # make a dict of the data
    histogram = dict()
    words = histogram.keys()
    for word in words_list:
        # for word in list:
        if word not in words:
            histogram[word] = 1
        else:
            histogram[word] += 1

    return histogram
    """


if __name__ == "__main__":
    print(histogram_as_dict(sys.argv[1]))
