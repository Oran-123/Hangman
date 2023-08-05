import random
import string
import sys
import gspread
import datetime
import getpass

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

LINES = Fore.GREEN + "-------------------------------------------------------------------------------\n-------------------------------------------------------------------------------"
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

leaderboard = SHEET.worksheet('leaderboard')

date = datetime.today().strftime('%Y-%m-%d')


def welcome_message():
    """
    Prints the welcome message letter by letter
    """
    print(Fore.GREEN + LOGO)
    print(Style.RESET_ALL)
    for letters in WELCOME:
        sleep(0.05)
        sys.stdout.write(letters)
        sys.stdout.flush()
    playgame_or_leaderboard()


def playgame_or_leaderboard():
    """
    Function enables the user to input the letter A or B
    Depending on the letter entered eithe the game or show leaderboard
    functions will be called
    """

    print(LINES)
    print(Style.RESET_ALL)
    print("A - PLAY GAME \nB - LEADERBOARD")
    print("\n")
    a_or_b_valid_response = False
    if a_or_b_valid_response is False:
        player_response = input(
            Fore.CYAN + "Enter A or B to continue:\n").upper()
        print(Style.RESET_ALL)
        print(LINES)
        print(Style.RESET_ALL)
        if player_response == "A":
            display_rules(Fore.GREEN + RULES)
            print(Style.RESET_ALL)
            a_or_b_valid_response = True
        elif player_response == "B":
            show_leaderboard()
            a_or_b_valid_response = True
        else:
            print(Fore.RED + "Invalid character entered, please enter either A or B")
            playgame_or_leaderboard()


def display_rules(rules):
    """
    Prints the rules of the game which are imported from
    rules.py
    """
    print(rules)
    start_game_valid_response = False
    if start_game_valid_response is False:
        start_game = getpass.getpass(Fore.CYAN + "Press ENTER to start the game:\n")
        print(Style.RESET_ALL)
        if start_game != "" or start_game == "":
            play_hangman()
            start_game_valid_response = True
        else:
            start_game_valid_response = False



def play_hangman():
    answer = 'TEST'
    answer_letters = list(answer)
    available_letters = list(string.ascii_uppercase)
    used_letters = []
    used_words = []
    lives = 7
    attempts = 0
    correct_response = None
    game_active = True
    response = ""

    username = get_username()

    while game_active:
        display_game_status(username, lives, attempts, answer, answer_letters, used_letters, used_words, response)

        selected_letter = get_selected_letter()

        selected_word = get_selected_word() 

        if selected_letter:
            response, lives, attempts = process_letter_guess(selected_letter, answer, answer_letters, used_letters, available_letters, response, lives, attempts)
        elif selected_word:
            response, lives, attempts = process_word_guess(selected_word, answer, response, lives, attempts,used_word)
        

        if all(letter in used_letters for letter in answer_letters):
            game_active = False
            final_result_won(lives, username, (lives * SCORE_PER_LIFE), len(answer_letters), answer)
            correct_response = " "
            update_leaderboard()
        elif lives == 0:
            game_active = False
            print(HANGMAN_STAGES[attempts])
            correct_response = " "
            final_result_lost(username, (lives * SCORE_PER_LIFE), answer)

def get_random_word(words):
    """
    picks a random word from the list of words
    and validates the word
    """
    random_word = random.choice(words)
    while "-" in random_word or " " in random_word:
        random_word = random.choice(words)
    return random_word.upper()

def get_username():
    while True:
        username = input(Fore.CYAN + "Enter your name:\n")
        print(Style.RESET_ALL)
        if len(username) > 0:
            return username
        else:
            print(Fore.RED + "Invalid username. Please enter a non-empty name.")

def display_game_status(username, lives, attempts, answer,answer_letters, used_letters, used_words, response):
    print(LINES)
    print(Style.RESET_ALL)
    print(HANGMAN_STAGES[attempts])
    print(Fore.RED + f'Used Letters: {used_letters}')
    print(Style.RESET_ALL)
    print(Fore.RED + f'Used Words: {used_words}')
    print(Style.RESET_ALL)
    hidden_answer_letters = [letter if letter in used_letters else "_" for letter in answer]
    print("Current Word:", " ".join(hidden_answer_letters))
    print(LINES)
    print(Style.RESET_ALL)
    if lives > 5:
        print(Fore.GREEN + f'{username} you have {lives} lives remaining')
    elif 6 > lives > 3:
        print(Fore.YELLOW + f'{username} you have {lives} lives remaining')
    elif lives < 4:
        print(Fore.RED + f'{username} you have {lives} lives remaining')
    print(Style.RESET_ALL)
    print(response)

def get_selected_letter():
    selected_letter = input("Guess a letter:\n").upper()
    return selected_letter

def get_selected_word():
    selected_word = input("Guess the word:\n").upper()
    return selected_word

def process_letter_guess(selected_letter, answer, answer_letters, used_letters, available_letters, response, lives, attempts):
    if len(selected_letter) == 1 and selected_letter.isalpha():
        if selected_letter in used_letters:
            response ="Oops... you have already selected {selected_letter}, try typing a different letter!"
            correct_response = None
        elif selected_letter not in used_letters:
            used_letters.append(selected_letter)
            if selected_letter in answer:
                available_letters.remove(selected_letter)
                answer_letters.remove(selected_letter)
                response = "Well done, that is correct!"
            else:
                response = "Oh no, that is incorrect!"
                lives -= 1
                attempts += 1
    else:
        response ="Invalid character. Please try typing a letter!"

    return response, lives, attempts
    

def process_word_guess(selected_word, answer, response, lives, attempts,used_word):
    if len(selected_word) == len(answer) and selected_word.isalpha():
        if selected_word == answer:
            response = "Well done, that is correct!"
            final_result()
        else:
            used_letters.append(selected_word)
            response = "Oh no, that is incorrect!"
            lives -= 1
            attempts += 1
    else:
        response ="Invalid character. Please try typing a letter!"

    return response, lives, attempts


# def play_hangman():
#     """
#     Main game function displays random word and enables user
#     to input guesses, also validates the users response
#     """
#     # get_random_word(random_words)
#     answer = 'TEST'
#     answer_letters = list(answer)
#     available_letters = list(string.ascii_uppercase)
#     used_letters = []
#     used_words = []

#     lives = 7
#     attempts = 0
#     correct_response = " "
#     game_active = True


#     while True:
#         username = input(Fore.CYAN + "Enter your name:\n")
#         print(Style.RESET_ALL)
#         if len(username) > 0:
#             break
#         else:
#             print(Fore.RED + "Invalid username. Please enter a non-empty name.")

#     while game_active:
#         print(LINES)
#         print(Style.RESET_ALL)

#         print(HANGMAN_STAGES[attempts])

#         print(Fore.RED + f'Used Letters: {used_letters}')
#         print(Style.RESET_ALL)

#         print(Fore.RED + f'Used Words: {used_words}')
#         print(Style.RESET_ALL)

#         hidden_answer_letters = [
#             letter if letter in used_letters else "_" for letter in answer]
#         print("Current Word:", " ".join(hidden_answer_letters))
#         print(LINES)
#         print(Style.RESET_ALL)

#         if lives > 5:
#             print(Fore.GREEN +
#                     f'{username} you have {lives} lives remaining')
#             print(Style.RESET_ALL)
#         elif 6 > lives > 3:
#             print(Fore.YELLOW +
#                     f'{username} you have {lives} lives remaining')
#             print(Style.RESET_ALL)
#         elif lives < 4:
#             print(
#                 Fore.RED + f'{username} you have {lives} lives remaining')
#             print(Style.RESET_ALL)
#         print("\n")
#         if correct_response is True:
#             print(Fore.GREEN + "Well done, that is correct!")
#             print(Style.RESET_ALL)
#         elif correct_response is False:
#             print(Fore.RED + "Oh no, that is incorrect!")
#             print(Style.RESET_ALL)
#         else:
#             print()

#         selected_letter = input("Guess a letter:\n").upper()
#         if len(selected_letter) == 1 and selected_letter.isalpha():
#             if selected_letter in used_letters:
#                 print(
#                     f"Oops... you have already selected {selected_letter}, try typing a different letter!")
#                 correct_response = " "
#             elif selected_letter not in used_letters:
#                 used_letters.append(selected_letter)
#                 if selected_letter in answer_letters:
#                     available_letters.remove(selected_letter)
#                     answer_letters.remove(selected_letter)
#                     correct_response = True
#                 elif selected_letter not in answer_letters:
#                     correct_response = False
#                     lives -= 1
#                     attempts += 1
#         elif len(selected_letter) == len(answer) and selected_letter.isalpha():
#             if selected_letter in used_words:
#                 print(
#                     f"Oops... you have already selected {selected_letter}, try typing a different letter!")
#             elif selected_letter not in used_words:
#                 used_words.append(selected_letter)
#                 if selected_letter == answer:
#                     correct_response = " "
#                     final_result()
#                 elif selected_letter != answer:
#                     used_words.append(selected_letter)
#                     correct_respons = False
#                     lives -= 1
#                     attempts += 1
#         else:
#             correct_response = " "
#             print("Invalid, character. Please try typing a letter!")
#     score = (lives * SCORE_PER_LIFE)
#     if len(answer_letters) == 0:
#         game_active = False
#         final_result_won(lives, username, score,
#                             len(answer_letters), answer)
#         correct_response = " "
#         upate_leaderboard()
#     elif lives == 0:
#         game_active = False
#         print(HANGMAN_STAGES[attempts])
#         correct_response = " "
#         final_result_lost(username, score, answer)


def final_result_lost(username, score, answer):
    """
    Prints personalised message in response to the users score
    """
    print(Fore.RED + LOSS)
    print(Style.RESET_ALL)
    print(
        f'Unfortunatley {username} you have met your faith, better luck next time!\nyou finished with a score of {score} points\n')
    print(f'The word was {answer}\n')
    play_again()


def final_result_won(lives, username, score, word_length, answer):
    """
    Prints ASCII art to highlight if the user won or lost the game
    """
    final_score = score + FULL_WORD_SCORE
    print(Fore.GREEN + VICTORY)
    print(Style.RESET_ALL)
    if lives == 7:
        final_score = final_score + UNSCATHED_SCORE
        print(
            Fore.GREEN + f'Wow.. {username} you survived without a scratch! \nyou finished with a score of {final_score} points\n')
        print(Style.RESET_ALL)
    elif 7 > lives > 3:
        final_score = final_score + HALF_OF_LIVES_REMAINING_BONUS
        print(
            Fore.GREEN + f'Congratulations {username} your survived with {lives} lives remaining, but you might not the text time! \nyou finished with a score of {final_score} points\n')
        print(Style.RESET_ALL)
    elif lives < 4:
        print(
            Fore.GREEN + f'That was close {username} you just made it with {lives} lives remaining, you got lucky this time! \nyou finished with a score of {final_score} points\n')
        print(Style.RESET_ALL)

    update_leaderboard(username, final_score)


def play_again():
    """
    Enables the user to select next action after the game finishes
    User can enter A,B or C and a different function will be called depending on input
    """
    print("What would you like to do next:\nA- Play Again\nB - Leaderboard\nC - Exit")
    play_again_valid_response = False
    if play_again_valid_response is False:
        selected_option = input(Fore.CYAN + "Enter Your Choice:\n").upper()
        print(Style.RESET_ALL)
        if selected_option == "A":
            play_hangman()
            play_again_valid_response is True
        elif selected_option == "B":
            show_leaderboard()
            play_again_valid_response is True
        elif selected_option == "C":
            exit()
            play_again_valid_response is True
        else:
            print("Invalid option selected, please try again and select A, B or C")
            play_again_valid_response is False


def update_leaderboard(username, score):
    """
    Updates the google sheet with the users score
    Called at the end of each game
    """
    data = [username, score, str(date)]
    print('Updating leaderborad....')
    leaderboard.append_row(data)
    print("\n")
    print('Leaderboard succesfully updated\n')
    play_again()


def show_leaderboard():
    """
    Prints the leaderboard using the ASCII art created in the leaderboard.py file
    """

    print(Fore.GREEN + "Loading leaderboard......")
    print(Style.RESET_ALL)
    sleep(2)
    leaderboard_data = leaderboard.get_all_values()
    results = leaderboard_data[1:]

    sorted_results = sorted(
        leaderboard_data, key=lambda x: int(x[1]), reverse=True)

    print(Fore.YELLOW + f'{LEADERBOARD}')
    print(Style.RESET_ALL)
    if (len(sorted_results) < 15):
        count_of_results = len(sorted_results)
    else:
        count_of_results = 15

    for i in range(0, count_of_results):
        print(f"""
        {i+1}\t{sorted_results[i][0]}    \t{sorted_results[i][1]}\t{sorted_results[i][2]}""")
        print(Fore.YELLOW + "===============================================================================")
        print(Style.RESET_ALL)
    print(Fore.GREEN + "Leaderboard loaded succesfully.")
    print(Style.RESET_ALL)
    leaderboard_options()


def leaderboard_options():
    """
    Enables the user to either exit or play the game again
    """
    print("What would you like to do next:\nA- Play Again\nB - Exit")
    play_again_valid_response = False
    if play_again_valid_response is False:
        selected_option = input(Fore.CYAN + "Enter Your Choice:\n").upper()
        print(Style.RESET_ALL)
        if selected_option == "A":
            play_hangman()
            play_again_valid_response is True
        elif selected_option == "B":
            exit()
            play_again_valid_response is True
        else:
            print("Invalid option selected, please try again and select A or B")
            play_again_valid_response is False


def main():
    welcome_message()


main()
