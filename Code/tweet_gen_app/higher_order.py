from markov_chain import MarkovChain
import clean_words
from dictogram import Dictogram
import random


class HigherMarkovChain(MarkovChain):
    pass


if __name__ == "__main__":
    left_right_list = ['I', 'went', 'left', 'you', 'went', 'right',
                       'I', 'went', 'left', 'I', 'went', 'right']
    mark = MarkovChain(left_right_list)
    print(mark.random_walk())
