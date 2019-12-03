from markov_chain import MarkovChain
import sys


class HigherMarkovChain(MarkovChain):
    def __init__(self, words_list=None, order=2):
        """Extends all the properties of a First Order MarkovChain.
           Adds a queue property for calculating probabilities for state
           transitions.

        """
        super().__init__(words_list)  # use a first order Markov Chain to start
        self.queue = list()
        self.order = order  # the number of word types held in a state
    """
    def populate_chain(self):
        '''Construct a dictionary to represent the MarkovChain state
           transitions of any order.

        '''
        pass
    """
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


if __name__ == "__main__":
    order_num = sys.argv[0:]
    left_right_list = ['I', 'went', 'left', 'you', 'went', 'right',
                       'I', 'went', 'left', 'I', 'went', 'right']
    mark = HigherMarkovChain(left_right_list, order=order_num)
    print(mark.random_walk())
