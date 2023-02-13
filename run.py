import random
import string
import sys
import gspread
import datetime 

from results import * 
from colorama import Fore, Back, Style
from leaderboard import LEADERBOARD
from logo import LOGO
from welcome_text import WELCOME
from rules import RULES
from datetime import datetime
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

date = datetime.today().strftime('%Y-%m-%d')


def welcome_message():
    print(Fore.GREEN + LOGO)
    print(Style.RESET_ALL)
    for letters in WELCOME:
        sleep(0.05)
        sys.stdout.write(letters)
        sys.stdout.flush()
    playgame_or_leaderboard()

def playgame_or_leaderboard():
    print("\n-------------------------------------------------------------------------------\n-------------------------------------------------------------------------------")
    print("A - PLAY GAME \nB - LEADERBOARD")
    a_or_b_valid_response = False
    while a_or_b_valid_response == False:
        player_response = input(Fore.YELLOW + "Enter A or B to continue:\n").upper()
        print(Style.RESET_ALL)
        print("-------------------------------------------------------------------------------\n-------------------------------------------------------------------------------")
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
        start_game = input(Fore.YELLOW +"Press any button to start the game:\n")
        print(Style.RESET_ALL)        
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

    correct_response = " " 
    
    #ask for username 
    username_valid_response = False

    while username_valid_response == False:
        username = input(Fore.YELLOW +"Enter your name:\n")
        print(Style.RESET_ALL)
        if len(username) > 0:
            username_valid_response = True
        else:
            username_valid_response = False
    

    while username_valid_response == True:
        # let user select letters until word is guessed correctly 
        while len(answer_letters) > 0 and lives > 0: 
            print("-------------------------------------------------------------------------------\n-------------------------------------------------------------------------------")
            #display art 
            print(HANGMAN_STAGES[attempts])
            

            #display the letters the user selected 
            print(Fore.RED + f'Used Letters: {used_letters}')
            print(Style.RESET_ALL)
            #dispaly guessed words
            print(Fore.RED + f'Used Words: {used_words}')
            print(Style.RESET_ALL)  
            #display the hidden word
            hidden_answer_letters = [letter if letter in used_letters else "_" for letter in answer]
            print("Current Word:" ," ".join(hidden_answer_letters) )
            print("-------------------------------------------------------------------------------\n-------------------------------------------------------------------------------")
            #display current lives 
            if lives > 5:
                print(Fore.GREEN + f'{username} you have {lives} remaining')
                print(Style.RESET_ALL)
            elif 6 > lives > 3:
                print(Fore.YELLOW + f'{username} you have {lives} remaining')
                print(Style.RESET_ALL)
            elif lives < 3:
                print(Fore.RED + f'{username} you have {lives} remaining')
                print(Style.RESET_ALL) 
            print("\n")
            if correct_response == True:
                print(Fore.GREEN + "Well done, that is correct!")
                print(Style.RESET_ALL)
            elif correct_response == False:
                print(Fore.RED + "Oh no, that is incorrect!")
                print(Style.RESET_ALL)
            else:
                print()
            #user input, and validation 
            selected_letter = input("Guess a letter:\n").upper()
            if len(selected_letter) == 1 and selected_letter.isalpha():
                if selected_letter in used_letters:
                    print(f"Oops... you have already selected {selected_letter}, try typing a different letter!")
                elif selected_letter not in used_letters:
                    used_letters.append(selected_letter)
                    if selected_letter in answer_letters:
                        available_letters.remove(selected_letter)
                        answer_letters.remove(selected_letter)
                        correct_response = True
                    elif selected_letter not in answer_letters:
                        correct_response = False
                        lives -= 1
                        attempts += 1  
            elif len(selected_letter) == len(answer) and selected_letter.isalpha():
                if selected_letter in used_words:
                    print(f"Oops... you have already selected {selected_letter}, try typing a different letter!")
                elif selected_letter not in used_words:
                    used_words.append(selected_letter)
                    if selected_letter == answer:
                        correct_response = " "
                        final_result()
                    elif selected_letter != answer:
                        used_words.append(selected_letter)
                        correct_respons = False
                        lives -= 1
                        attempts += 1  
            else: 
                print("Invalid, character. Please try typing a letter!")     
        score = (lives * SCORE_PER_LIFE) 
        if len(answer_letters) == 0:
            final_result_won(lives, username, score,len(answer_letters))
            correct_response = " "
            upate_leaderboard()
        elif lives == 0:
            print(HANGMAN_STAGES[attempts])
            correct_response = " "
            final_result_lost(username,score)            
        
def final_result_lost(username, score):
    print(Fore.RED + LOSS)
    print(Style.RESET_ALL)
    print(f'Unfortunatley {username} you have met your faith, better luck next time!\nyou finished with a score of {score} points\n')
    play_again()
    
def final_result_won(lives,username,score,word_length):
    final_score = score + FULL_WORD_SCORE
    print(Fore.GREEN + VICTORY)
    print(Style.RESET_ALL)
    if lives == 7:
        final_score = final_score + UNSCATHED_SCORE 
        print(Fore.GREEN + f'Wow.. {username} you survived without a scratch! \nyou finished with a score of {final_score} points\n') 
        print(Style.RESET_ALL)
    elif 7 > lives > 3:
        final_score = final_score + HALF_OF_LIVES_REMAINING_BONUS
        print(Fore.GREEN + f'Congratulations {username} your survived with {lives} remaining, but you might not the text time! \nyou finished with a score of {final_score} points\n') 
        print(Style.RESET_ALL)
    elif lives < 4:
        print(Fore.GREEN + f'That was close {username} you just made it with {lives} remaining, you got lucky this time! \nyou finished with a score of {final_score} points\n') 
        print(Style.RESET_ALL)

    upate_leaderboard(username, final_score)
    
def play_again():
    print("What would you like to do next:\nA- Play Again\nB - Leaderboard\nC - Exit")
    play_again_valid_response = False
    while play_again_valid_response == False:
        selected_option = input(Fore.YELLOW + "Enter Your Choice:\n").upper()
        print(Style.RESET_ALL)
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
    data = [username, score, str(date)]
    print('Updating leaderborad....')
    leaderboard.append_row(data)
    print("\n")
    print('Leaderboard succesfully updated\n')
    play_again()
    
def show_leaderboard():
    
    print(Fore.GREEN + "Loading leaderboard......")
    print(Stlye.RESET_ALL)
    sleep(2)
    leaderboard_data = leaderboard.get_all_values()    
    results = leaderboard_data[1:]

    sorted_results = sorted(leaderboard_data, key=lambda x: int(x[1]), reverse=True)

    print(Fore.YELLOW + f'{LEADERBOARD}')
    print(Stlye.RESET_ALL)
    if(len(sorted_results) < 15):
        count_of_results = len(sorted_results)
    else:
        count_of_results = 15

    for i in range(0, count_of_results):
        print(f"""
        {i+1}\t{sorted_results[i][0]}    \t{sorted_results[i][1]}\t{sorted_results[i][2]}""")
        print(Fore.CYAN + "===============================================================================")
        print(Stlye.RESET_ALL)
    print(Fore.GREEN + "Leaderboard loaded succesfully.")
    print(Stlye.RESET_ALL)
    leaderboard_options()


def leaderboard_options():
    print("What would you like to do next:\nA- Play Again\nB - Exit")
    play_again_valid_response = False
    while play_again_valid_response == False:
        selected_option = input(Fore.YELLOW + "Enter Your Choice:\n").upper()
        print(Stle.RESET_ALL)
        if selected_option == "A":
            play_hangman()
            play_again_valid_response == True
        elif selected_option == "B":
            exit()
            play_again_valid_response == True
        else:
            print("Invalid option selected, please try again and select A or B")
            play_again_valid_response == False

def main ():
    welcome_message()

main()




