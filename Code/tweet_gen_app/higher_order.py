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
        """Add the item to the end of the current queue.
           0(1) runtime.

        """
        self.queue.append(item)

    def dequeue(self):
        """Return the first item in the queue.
           Raises IndexErrorif there are no items.
           0(1) runtime.

        """
        if not len(self.queue) == 0:
            item = self.queue.pop(0)
            return item
        else:
            raise IndexError('There are currently no items in the queue.')

    def iterate_queue(self):
        """Returns an iterable of the items in the queue.
           Raises IndexError if there are no items.
           O(n) runtime.

        """
        if not len(self.queue) == 0:
            for item in self.queue:
                yield(item)
        else:
            raise IndexError('There are currently no items in the queue.')


if __name__ == "__main__":
    left_right_list = ['I', 'went', 'left', 'you', 'went', 'right',
                       'I', 'went', 'left', 'I', 'went', 'right']
    mark = HigherMarkovChain(left_right_list)
    mark.queue = ['a', 'b', 'c']
    for item in mark.queue:
        print(item)
