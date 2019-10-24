import sys


def remove_newlines(list_of_lists):
    """Remove newline characters from a list of lists containing strings."""
    newline_list = ["\n"]  # what we don't want
    for list in list_of_lists:
        if list == newline_list:
            list_of_lists.remove(list)
    return list_of_lists


def histogram_as_dict(file_name):
    """Return a histogram of the appearances of words from a .txt file.
       Param: file_name(str): name of file with source text (.txt)
       Return: histogram(dict): every key a unique word, value is appearances
               of the word in the text
    """
    with open(file_name) as file:
        words = [line.split(" ") for line in file.readlines()]
    words = remove_newlines(words)
    print(words)


if __name__ == "__main__":
    histogram_as_dict(sys.argv[1])
