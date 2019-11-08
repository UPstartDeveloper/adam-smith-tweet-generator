import tweet_gen_app.clean_words as cw
from tweet_gen_app.dictogram import Dictogram


class MarkovChain:
    def __init__(self, words_list=None):
        """Construct a Markov Chain model."""
        # create a list of words from the corpus
        self.words_list = list()
        if words_list is None:
            self.words_list = cw.get_clean_words  # use adam smith corpus
        # keys in the self.states dict
        self.types = (
            [word for word in self.words_list if word not in self.types]
        )
        # create a dict to store all types and their state histograms
        self.states = dict()
        for type in self.types:
            tokens_that_follow = list()
            for index in range(len(self.words_list)):
                word = self.words_list[index]
                word_before = self.words_list[index - 1]
                if not index == 0 and word_before == type:
                    tokens_that_follow.append(word_before)
            self.states[type] = Dictogram(tokens_that_follow)

    def random_walk(self, length=10):
        """Generate a sentence by randomly transitioning between states.
           Param: length(int) the number of words that should be generated
           Return: sentence(str)
        """
        pass
