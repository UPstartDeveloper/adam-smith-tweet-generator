from markov_chain import MarkovChain
import unittest


class MarkovChainTest(unittest.TestCase):
    def test_init(self):
        '''Checks that the Markov Chain represents the corpus correctly.'''
        fish_list = [
            "one", "fish", "two", "fish", "red", "fish", "blue", "fish"
        ]
        mark = MarkovChain(fish_list)

        # test for the correct number of keys in the Markov Chain object
        states_of_fish_list = len(set(fish_list))
        states_of_mark = len(mark.chain.keys())
        assert states_of_mark == states_of_fish_list

        # test for the correct number of state transitions
        tokens = len(fish_list)
        number_of_state_transitions = 0
        states = list(mark.chain.keys())
        for state in states:
            tokens_after_state = 0
            transitions_for_one_state = mark.chain[state]
            states_after = list(transitions_for_one_state.keys())
            for word_type in states_after:
                tokens_after_state += transitions_for_one_state[word_type]
            # print(transitions_for_one_state.values())
            # number_of_state_transitions += (
            #    transitions_for_one_state.values())
            number_of_state_transitions += tokens_after_state
        assert tokens == number_of_state_transitions

    def test_random_walk(self):
        '''The sentence generated follows the Markov Chain algorithm.'''
        fish_list = [
            "one", "fish", "two", "fish", "red", "fish", "blue", "fish"
        ]
        mark = MarkovChain(fish_list)
        pass




if __name__ == "__main__":
    unittest.main()
