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
    available_letters = list(strng.ascii_uppercase)
    used_letters = []

    #user input, and validation 
    selected_letter = input("Guess a letter: ").upper()
    if selected_letter not in used_letters:
        used_letters.append(selected_letter)
        if selected_letter in word_letters:
            available_letters.remove(selected_letter)
            print("Well done, that is correct!")
    elif selected_letter in used_letters:
        print("Oops... you have already selected this letter, try typing a different letter!")
    else:
        print("Invalid, character. Please try typing a letter!")

