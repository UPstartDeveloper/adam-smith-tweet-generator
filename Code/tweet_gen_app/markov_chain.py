import clean_words
from dictogram import Dictogram
import random


class MarkovChain:
    def __init__(self, words_list=None):
        """Construct a Markov Chain model.
           Param: words_list(list of str)
        """
        # create a list of words from the corpus
        self.words_list = list()
        if words_list is None:
            # using adam smith corpus
            self.words_list = clean_words.get_clean_words()
        else:
            # use the passed in list of words
            self.words_list = words_list
        # keys in the self.states dict
        self.types_of_words = list()
        self.types_of_words = (
            [word for word in self.words_list if word not
             in self.types_of_words]
        )
        # create a dict to store all types and their state histograms
        self.states = dict()
        for type in self.types_of_words:
            tokens_that_follow = list()
            for index in range(len(self.words_list)):
                word = self.words_list[index]
                word_before = self.words_list[index - 1]
                if not index == 0 and word_before == type:
                    tokens_that_follow.append(word)
            self.states[type] = Dictogram(tokens_that_follow)

    def random_walk(self, length=10):
        """Generate a sentence by randomly transitioning between states.
           Param: length(int) the number of words that should be generated
           Return: sentence(str)
        """
        # pick a word randomly to start the sentence
        state_types = self.states.keys()
        sentence = ''
        first_word = random.sample(state_types, 1)[0]
        sentence += first_word + " "
        # start the random walk
        next_word = first_word
        for i in range(length - 1):
            # make sure the word has tokens that come after, find the next word
            if self.states[next_word] is not None:
                next_word = self.states[next_word].sample()
            else:
                next_word = random.sample(state_types, 1)[0]
            sentence += next_word + " "
        return sentence


if __name__ == "__main__":
    fish_list = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
    mark = MarkovChain(fish_list)
    print(mark.random_walk())
