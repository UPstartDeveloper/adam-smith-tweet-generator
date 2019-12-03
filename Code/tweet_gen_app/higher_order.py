from markov_chain import MarkovChain
import clean_words
from dictogram import Dictogram
import random


class HigherMarkovChain(MarkovChain):
    def __init__(self, words_list=None):
        """Extends all the properties of a First Order MarkovChain.
           Adds a queue property for calculating probabilities for state
           transitions.

        """
        super().__init__(words_list)  # use a first order Markov Chain to start
        self.queue = list()

    def enqueue(self, item):
        '''Add the item to the end of the current queue.'''
        self.queue.append(item)

    def dequeue(self):
        '''Return the first item in the queue. Raises if there are no items.'''
        if not len(self.queue) == 0:
            item = self.queue.pop(0)
            return item
        else:
            raise IndexError('There are currently no items in the queue.')

    def __iter__(self):
        '''Returns an iterable of the items in the queue.'''
        if not len(self.queue) == 0:
            return iter(self.queue)
        else:
            raise IndexError('There are currently no items in the queue.')


if __name__ == "__main__":
    left_right_list = ['I', 'went', 'left', 'you', 'went', 'right',
                       'I', 'went', 'left', 'I', 'went', 'right']
    mark = HigherMarkovChain(left_right_list)
