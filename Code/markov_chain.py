import tweet_gen_app.clean_words as cw
import tweet_gen_app.dictogram as dictogram


class MarkovChain:
    def __init__(self, words_list=None):
        """Construct a Markov Chain model."""
        # create a list of words from the corpus
        self.words_list = list()
        if words_list is None:
            self.words_list = cw.get_clean_words  # use adam smith corpus
        # create a dict to store all types and their state histograms
        self.types = (
            [word for word in self.words_list if word not in self.types]
        )
        self.states = dict()
        for word in self.types:
            self.states[word] = 0
