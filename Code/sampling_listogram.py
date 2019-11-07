from tweet_gen_app.stochastic_sampling import *


def weighted_sample(histogram):
    """Chooses a random word from the histogram of word frequency.
       Words that have higher frequnecy counts in the histogram will
       be chosen more often by this function.
       Param: histogram(list of lists)
       Return: word(str)
    """
    
