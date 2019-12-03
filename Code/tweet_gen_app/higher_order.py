from markov_chain import MarkovChain
import sys
from dictogram import Dictogram


class HigherMarkovChain(MarkovChain):
    def __init__(self, words_list=None, order=2):
        """Extends all the properties of a First Order MarkovChain.
           Adds a queue property for calculating probabilities for state
           transitions.

           Parameters:
           words_list(list): a list of str represen the corpus text
           order(int): the number of word types held in a state

        """
        self.queue = list()
        self.order = order
        # initialize self.words_list and self.chain
        super().__init__(words_list)

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
        # define the next state
        next_state = list()
        # add the tokens that begin this state
        next_state.extend(words_in_between)
        # add the last token that defines this state
        next_state.append(self.dequeue())
        # return the state
        next_state = tuple(next_state)
        return next_state

    def form_states(self, index):
        """Assists in forming states based on the order of the Markov Chain.

           Parameters:
           self(HigherMarkovChain): the instance of the class
           index(int): the position currently being examined in the corpus

           Returns:
           tuple: consists of tuples representing adjacent states

        """
        # add tokens for the new state to the queue
        for j in range(self.order):
            self.enqueue(self.words_list[index])
            index += 1
        # define the new state
        state, words_in_between = self.form_first_state()
        # define the next state, start by "backpeddalling" the index position
        index -= 1
        self.enqueue(self.words_list[index + 1])
        next_state = self.form_next_state(words_in_between)
        # return both states
        return (state, next_state)

    def populate_chain(self):
        """Construct a dictionary to represent the MarkovChain state
           transitions of any order.

        """
        chain = dict()
        i = 0
        while i < len(self.words_list) - self.order:  # avoid IndexError at end
            state, state_after = self.form_states(i)
            # create a word frequency dict to go along with each state
            if chain.get(state, None) is None:
                list_of_states = []
                list_of_states.append(state_after)
                chain[state] = Dictogram(list_of_states)
            # if the state already exists, add the token and count
            else:
                chain[state].add_count(state_after)
            i += 1  # move index over to start recording of next state
        return chain

    def random_walk(self, length=10):
        """Generate a sentence by randomly transitioning between states.
           Implements safeguards to avoid repeating words.

           Parameters:
           length(int): number of words to be generated

           Returns:
           str: a sequence of word tokens originally from the corpus
        """
        pass


if __name__ == "__main__":
    left_right_list = ['I', 'went', 'left', 'you', 'went', 'right',
                       'I', 'went', 'left', 'I', 'went', 'right']
    if len(sys.argv) > 1:  # user-defined order for the Markov Chain
        order_num = int(sys.argv[1])
        mark = HigherMarkovChain(left_right_list, order_num)
    else:  # defaults to Second Order Markov Chain
        mark = HigherMarkovChain(left_right_list)
    print(mark.random_walk())
