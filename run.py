import random
import string
import sys
import gspread
import datetime 

from random_words import random_words
from hangman_art import HANGMAN_STAGES
from time import sleep
from google.oauth2.service_account import Credentials

UNSCATHED_SCORE = 100 
FULL_WORD_SCORE = 50 
HALF_OF_LIVES_REMAINING_BONUS = 25 
SCORE_PER_LIFE = 10  
SCORE_PER_LETTER = 5 

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman-leaderboard')

leaderboard =  SHEET.worksheet('leaderboard')
leaderboard_data = leaderboard.get_all_values()

date = datetime.datetime.now()

RULES = """
The rules are simple:\n
\n
1. Guess the word by typing a letter\n
2. If you choose a letter that is not in the word you loose a life\n
3. If you guess the word before all your lives are up you win\n 
4. If you run out of lives before you guess the word you die\n 
"""

def welcome_message():
    print("hangman art")
    welcome_text = "This is just a test\n"
    for letters in welcome_text:
        sleep(0.2)
        sys.stdout.write(letters)
        sys.stdout.flush()
    playgame_or_leaderboard()

def playgame_or_leaderboard():
    print("A - PLAY GAME \nB - LEADERBOARD")
    a_or_b_valid_response = False
    while a_or_b_valid_response == False:
        player_response = input("Enter A or B to continue:\n").upper()
        if player_response == "A":
            display_rules(RULES)
            a_or_b_valid_response = True
        elif player_response == "B":
            print("display leaderboard")
            a_or_b_valid_response = True
        elif player_response != "A" or player_response != "B":
            print ("Invalid character entered, please enter either A or B")
            a_or_b_valid_response = False 

def display_rules(rules):
    print(rules)
    start_game_valid_response = False
    while start_game_valid_response == False:
        start_game = input("Press any button to start the game:\n")
        if len(start_game) > 0:
            play_hangman()
            start_game_valid_response = True
        else:
            start_game_valid_response = False

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
    
    #ask for username 
    username_valid_response = False

    while username_valid_response == False:
        username = input("Enter your name:\n")
        if len(username) > 0:
            username_valid_response = True
        else:
            username_valid_response = False
    

    while username_valid_response == True:
        # let user select letters until word is guessed correctly 
        while len(answer_letters) > 0 and lives > 0: 

            #display art 
            print(HANGMAN_STAGES[attempts])
            #display current lives 
            print(f'{username} you have {lives} remaining')

            #display the letters the user selected 
            print(f'Used Letters: {used_letters}')

            #dispaly guessed words
            print(f'Used Words: {used_words}')

            #display the hidden word
            hidden_answer_letters = [letter if letter in used_letters else "_" for letter in answer]
            print("Current Word:" ," ".join(hidden_answer_letters) )

            #user input, and validation 
            selected_letter = input("Guess a letter:\n").upper()
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
                if selected_letter in used_words:
                    print(f"Oops... you have already selected {selected_letter}, try typing a different letter!")
                elif selected_letter not in used_words:
                    used_words.append(selected_letter)
                    if selected_letter == answer:
                        print("Well done, that is correct!")
                        final_result()
                    elif selected_letter != answer:
                        used_words.append(selected_letter)
                        print("Oh no, that is incorrect!")
                        lives -= 1
                        attempts += 1  
            else: 
                print("Invalid, character. Please try typing a letter!")     
        score = (lives * SCORE_PER_LIFE) 
        if lives == 0:
            print(HANGMAN_STAGES[attempts])
            final_result_lost(username,score)
        
        if "_" not in hidden_answer_letters:
            final_result_won(username,lives, attempts,len(answer_letters))
        upate_leaderboard()
        
def final_result_lost(username, score):
    print(f'Unfortunatley {username} you have met your faith, better luck next time!you finished with a score of {score} points\n')
    play_again()
    
def final_result_won(lives,username,score,word_length):
    if lives == 7:
        final_score = final_score + UNSCATHED_SCORE
        print(f'Wow.. {username} you survived without a scratch! you finished with a score of {final_score} points\n') 
    elif 7 < lives < 3:
        final_score = final_score + HALF_OF_LIVES_REMAINING_BONUS
        print(f'Congratulations {username} your survived with {lives} remaining, but you might not the text time! you finished with a score of {final_score} points\n') 
    elif lives < 4:
        print(f'That was close {username} you just made it with {lives} remaining, you got lucky this time! you finished with a score of {final_score} points\n') 
    
    play_again()

    
def play_again():
    print("What would you like to do next:\nA- Play Again\nB - Leaderboard\nC - Exit")
    play_again_valid_response = False
    while play_again_valid_response == False:
        selected_option = input("Enter Your Choice:\n").upper()
        if selected_option == "A":
            play_hangman()
            play_again_valid_response == True
        elif selected_option == "B":
            show_leaderboard()
            play_again_valid_response == True
        elif selected_option == "C":
            exit()
            play_again_valid_response == True
        else:
            print("Invalid option selected, please try again and select A, B or C")
            play_again_valid_response == False


def upate_leaderboard(username,score):
    data = [username, score, date]
    print('Updating leaderborad....')
    leaderboard.append_row(data)
    
def show_leaderboard():
    print("display leaderboard")

def main ():
    welcome_message()

main()