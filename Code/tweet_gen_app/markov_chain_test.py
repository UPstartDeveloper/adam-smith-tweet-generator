from markov_chain import MarkovChain
import unittest


class MarkovChainTest(unittest.TestCase):
    def test_init(self):
        '''Checks that the Markov Chain represents the corpus correctly.'''
        fish_list = [
            "one", "fish", "two", "fish", "red", "fish", "blue", "fish"
        ]
        mark = MarkovChain(fish_list)
        pass

    def test_random_walk(self):
        '''The sentence generated follows the Markov Chain algorithm.'''
        fish_list = [
            "one", "fish", "two", "fish", "red", "fish", "blue", "fish"
        ]
        mark = MarkovChain(fish_list)
        pass


if __name__ == "__main__":
    unittest.main()
