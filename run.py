import random
import string
import sys
from random_words import random_words
from hangman_art import HANGMAN_STAGES
from time import sleep


RULES = 
"""
The rules are simple:\n
\n
1. Guess the word by typing a letter 
2. If you choose a letter that is not in the word you loose a life\n
3. If you guess the word before all your lives are up you win\n 
4. If you run out of lives before you guess the word you die\n 
\n 
""""

def welcome_message():
    print("hangman art")
    welcome_text = "This is just a test\n"
    for letters in welcome_text:
        sleep(0.2)
        sys.stdout.write(letters)
        sys.stdout.flush()

def playgame_or_leaderboard():
    print("A - PLAY GAME \nB - LEADERBOARD")
    valid_response = False
    while valid_response == False:
        player_response = input("Enter A or B to continue: ").upper()
        if player_response == "A":
            display_rules(RULES)
            valid_response = True
        elif player_response == "B":
            print("display leaderboard")
            valid_response = True
        elif player_response != "A" or player_response != "B":
            print ("Invalid character entered, please enter either A or B")
            valid_response = False 

def display_rules(rules):
    print(rules)
    start_game = input("Press any button to start the game: ")
    if len(start_game) > 0:
        play_hangman()

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
    used_words = []

    # user lives 
    lives = 7 
    attempts = 0 
    
    # let user select letters until word is guessed correctly 
    while len(answer_letters) > 0 and lives > 0: 

        #display art 
        print(HANGMAN_STAGES[attempts])
        #display current lives 
        print(lives)

        #display the letters the user selected 
        print(f'Used Letters: {used_letters}')

        #dispaly guessed words
        print(f'Used Words: {used_words}')

        #display the hidden word
        hidden_answer_letters = [letter if letter in used_letters else "_" for letter in answer]
        print("Current Word:" ," ".join(hidden_answer_letters) )

        #user input, and validation 
        selected_letter = input("Guess a letter: ").upper()
        if len(selected_letter) == 1 and selected_letter.isalpha():
            if selected_letter in used_letters:
                print(f"Oops... you have already selected {selected_letter}, try typing a different letter!")
            elif selected_letter not in used_letters:
                used_letters.append(selected_letter)
                if selected_letter in answer_letters:
                    available_letters.remove(selected_letter)
                    print("Well done, that is correct!")
                elif selected_letter not in answer_letters:
                    print("Oh no, that is incorrect!")
                    lives -= 1
                    attempts += 1  
        elif len(selected_letter) == len(answer) and selected_letter.isalpha():
            if selected_letter in used_letters:
                print(f"Oops... you have already selected {selected_letter}, try typing a different letter!")
            elif selected_letter not in used_letters:
                used_letters.append(selected_letter)
                if selected_letter == answer:
                    print("Well done, that is correct!")
                elif selected_letter != answer:
                    used_words.append(selected_letter)
                    print("Oh no, that is incorrect!")
                    lives -= 1
                    attempts += 1  
        else: 
            print("Invalid, character. Please try typing a letter!")     
       
playgame_or_leaderboard()