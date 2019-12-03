from markov_chain import MarkovChain
import sys
from dictogram import Dictogram


class HigherMarkovChain(MarkovChain):
    def __init__(self, words_list=None, order=2):
        """Extends all the properties of a First Order MarkovChain.
           Adds a queue property for calculating probabilities for state
           transitions.

        """
        super().__init__(words_list)  # use a first order Markov Chain to start
        self.queue = list()
        self.order = order  # the number of word types held in a state

    def enqueue(self, *items):
        """Add the item to the end of the current queue.
           0(1) runtime.

        """
        self.queue.extend(*items)

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

    def form_state(self, index):
        """Assists in forming states based on the order of the Markov Chain.

           Parameters:
           self(HigherMarkovChain): the instance of the class
           index(int): the position currently being examined in the corpus

           Returns:
           tuple: consists of tuples representing adjacent states

        """
        return (1, 2)

    def populate_chain(self):
        """Construct a dictionary to represent the MarkovChain state
           transitions of any order.

        """
        chain = dict()
        i = 0
        while i < len(self.words_list) - 1:  # avoid IndexError at end of list
            state, state_after = self.form_state(i)
            # create a word frequency dict to go along with each state
            if chain.get(state, None) is None:
                chain[state] = Dictogram([state_after])
            # if the state already exists, add the token and count
            else:
                chain[state].add_count(state_after)
            i += self.order  # move index over to start recording of next state
        return chain


if __name__ == "__main__":
    order_num = sys.argv[0:]
    left_right_list = ['I', 'went', 'left', 'you', 'went', 'right',
                       'I', 'went', 'left', 'I', 'went', 'right']
    mark = HigherMarkovChain(left_right_list, order_num)
    print(mark.random_walk())
