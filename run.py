import random
import string
from random_words import random_words

def get_random_word(words):
    """ 
    picks a random word from the list of words
    and validates the word 
    """
    random_word = random.choice(words)
    while "-" in random_word or " " in random_word:
        random_word = random.choice(words)
    return random_word

def play_hangman():
        word = get_random_word(random_words)
        word_letters = list(word)


