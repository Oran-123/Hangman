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
    return random_word.upper()

def play_hangman():

    #defined game varriables 
    answer = get_random_word(random_words)
    answer_letters = list(answer)
    available_letters = list(string.ascii_uppercase)
    used_letters = []

    # user lives 
    lives = 7 

    # let user select letters until word is guessed correctly 
    while len(answer_letters) > 0 and lives > 0: 

        #display current lives 
        print(lives)

        #display the letters the user selected 
        print(f'Used Letters: {used_letters}')

        #display the hidden word
        hidden_answer_letters = [letter if letter in used_letters else "_" for letter in answer]
        print("Current Word:" ," ".join(hidden_answer_letters) )

        #user input, and validation 
        selected_letter = input("Guess a letter: ").upper()
        if selected_letter in used_letters:
            print("Oops... you have already selected this letter, try typing a different letter!")
        elif selected_letter not in available_letters:
            print("Invalid, character. Please try typing a letter!")
        elif selected_letter not in used_letters:
            used_letters.append(selected_letter)
            if selected_letter in answer_letters:
                available_letters.remove(selected_letter)
                print("Well done, that is correct!")
            elif selected_letter not in answer_letters:
                print("Oh no, that is incorrect!")
                lives -= 1
         
       

play_hangman()