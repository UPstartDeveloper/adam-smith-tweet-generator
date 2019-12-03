import clean_words
from dictogram import Dictogram
import random


class MarkovChain:
    def __init__(self, words_list=None):
        """Construct a Markov Chain model.
           Param: words_list(list of str)

        """
        # use the passed in list of words
        if words_list is not None:
            self.words_list = words_list
        else:
            # use the Adam Smith corpus
            self.words_list = clean_words.get_clean_words()
        # populate the Markov Chain
        self.chain = dict()
        self.chain = self.populate_chain()

    def populate_chain(self):
        """Construct a dictionary representing the conditional probabilities
           of transitioning from a given state in the word corpus to the next.

           Parameters: MarkovChain object

           Returns: (dict): where each key is a state, and each value
                            is a nested dict containing the transitions
                            out of that state, with int counts of their
                            appearances after the state in the corpus

        """
        chain = dict()
        i = 0
        while i < len(self.words_list) - 1:  # avoiding IndexError
            state = self.words_list[i]
            token_after = self.words_list[i + 1]
            # create a word frequency dict to go along with each state
            if chain.get(state, None) is None:
                chain[state] = Dictogram([token_after])
            # if the state already exists, add the token and count
            else:
                chain[state].add_count(token_after)
            i += 1
        return chain

    def random_walk(self, length=10):
        """Generate a sentence by randomly transitioning between states.
           Param: length(int) the number of words that should be generated
           Return: sentence(str)
        """
        # pick a word randomly to start the sentence
        state_types = self.chain.keys()
        sentence = ''
        first_word = random.sample(state_types, 1)[0]
        sentence += first_word + " "
        # start the random walk
        next_word = first_word
        for i in range(length - 1):
            # make sure the word has tokens that come after, find the next word
            if self.chain[next_word] is not None:
                next_word = self.chain[next_word].sample()
            else:
                next_word = random.sample(state_types, 1)[0]
            sentence += next_word + " "
        return sentence


if __name__ == "__main__":
    fish_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    mark = MarkovChain(fish_list)
    print(mark.random_walk())
