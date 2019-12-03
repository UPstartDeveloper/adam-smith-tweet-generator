from markov_chain import MarkovChain
import sys
from dictogram import Dictogram


class HigherMarkovChain(MarkovChain):
    def __init__(self, words_list=None, order=2):
        """Extends all the properties of a First Order MarkovChain.
           Adds a queue property for calculating probabilities for state
           transitions.

        """
        self.queue = list()
        self.order = order  # the number of word types held in a state
        super().__init__(words_list)  # initialize self.words_list

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

    def form_first_state(self):
        """Return a tuple of the words stored in the state currently being
           examined in the Markov self.chain structure.

           Parameters:
           self: a HigherMarkovChain instance

           Returns:
           tuple: contains a tuple of the state,
                  and a list of words to reuse in forming the following state

        """
        # add the first word to the state being formed
        state = list()
        state.append(self.dequeue())
        # define the words reused between this state add the next state
        words_in_between = list()
        for i in range(self.order - 1):
            words_in_between.append(self.dequeue())
        # add the rest of the words that belong in this state
        state.extend(words_in_between)
        # return values
        state = tuple(state)
        return (state, words_in_between)

    def form_next_state(self, words_in_between):
        """
        Define the state, which the state currently being examined, transitions
        to in the word corpus.

        Parameters:
        words_in_between(list): every word after the first token in the
                                previous state

        Returns:
        tuple: stores the tokens which belong in this state

        """
        pass

    def form_states(self, index):
        """Assists in forming states based on the order of the Markov Chain.

           Parameters:
           self(HigherMarkovChain): the instance of the class
           index(int): the position currently being examined in the corpus

           Returns:
           tuple: consists of tuples representing adjacent states

        """
        for j in range(self.order):
            self.enqueue(self.words_list[index])
        state, words_in_between = self.form_first_state()
        next_state = self.form_next_state(words_in_between)
        return (state, next_state)
        '''
        # form the current state we want to examine
        for j in range(index, index + self.order):
            self.enqueue(self.words_list[j])
        state = list()
        for k in range(self.order):
            state.append(self.dequeue())
        # make it usuable as a dict key
        state = tuple(state)
        # form the state that follows
        state_after = list()
        next_token = self.words_list[index + self.order]
        state_after = list(state[0:]).extend(list(next_token))
        print(f'state_after: {state_after}')
        # return both states
        return (state, state_after)
        '''

    def populate_chain(self):
        """Construct a dictionary to represent the MarkovChain state
           transitions of any order.

        """
        chain = dict()
        i = 0
        while i < len(self.words_list) - 1:  # avoid IndexError at end of list
            state, state_after = self.form_states(i)
            # create a word frequency dict to go along with each state
            if chain.get(state, None) is None:
                chain[state] = Dictogram([state_after])
            # if the state already exists, add the token and count
            else:
                chain[state].add_count(state_after)
            i += self.order  # move index over to start recording of next state
        return chain


if __name__ == "__main__":
    order_num = int(sys.argv[1])
    left_right_list = ['I', 'went', 'left', 'you', 'went', 'right',
                       'I', 'went', 'left', 'I', 'went', 'right']
    mark = HigherMarkovChain(left_right_list, order_num)
    print(mark.random_walk())
