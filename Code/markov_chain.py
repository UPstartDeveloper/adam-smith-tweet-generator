import tweet_gen_app.clean_words as cw


class MarkovChain:
    def __init__(self, words_list=None):
        if words_list is None:
            self.words_list = cw.get_clean_words  # use adam smith corpus
