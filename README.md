# Goal For This Project 

This Project will be a text-based python game where the user guesses the letters that make up a word before their lives run out. To win the game, the user must guess all the letters before they run out of lives. The user receives a score based on them guessing the word correctly and the number of lives they have remaining. There are bonus scores for guessing the word without losing a single life or if the user has more than four lives remaining. The user must try to finish the game with the highest score possible. 

![Goals for this project image](/documents/images/ui.png)


# Table of Contens 

* [UX](#ux "UX")
    * [User Goals](#user-goals "User Goals")
    * [User Stories](#user-stories "User Stories")
    * [Site owner Goals](#site-owner-goals "Site owner Goals")
* [Requirements and Expectations](#requirements-and-expectations "Requirements and Expectations")
    * [Requirements](#Requirments "Requirements")
    * [Expectations](#expectations "Expectations")
    * [How-To-Play](#how-to-play "How To Play")
* [Design-Choices](#design-choices "Design Choices")
    * [Fonts](#fonts "Fonts")
    * [Colours](#colours "Colors")
    * [Process](#process "Process")
* [Features](#features "Features")
    * [Existing-Features](#existing-features "Existing Feautres")
        * [Start-Game-Button](#start-game-button "Start Game Button")
        * [Game-Logo](#game-logo "Game Logo")
        * [Welcome-Message](#welcome-message "Welcome Message")
        * [Game-Rules](#game-rules "Game Rules")
        * [Enter-Username](#enter-username "Enter Username")
        * [Hidden-Letters](#hidden-letters "Hidden Letters")
        * [User-Letters/Words](#used-letters/words "User Letters and Words")
        * [Lives Remaining](#lives-remaining "Lives Remaining")
        * [Response-To-Correct/Incorrect-Letters](#response-to-correct/incorrect-letters "Response To Correct/Incorrect Letters")
        * [Score](#score "Score")
        * [Result](#result "Result")
        * [Leaderboard](#leaderboard "Leaderboard")
    * [Features-To-Be-Implemented](#features-to-be-implemented "Features to be Implemented")
        * [Difficulty-Levels](#difficulty-levels "Difficulty Levels")
* [Testing](#testng "Testing")
    * [UAT](#uat "UAT")
    * [Code-Validation](#code-validation "Code Validation")
    * [Contrast-Testing](#contrast-testing "Contrast Testing")
    * [Resolve-Bugs](#resolved-bugs "Resoloved Bugs")
    * [open-Bugs](#open-bugs "open Bugs")
* [Technologies](#technologies "Technologies")
    * [Languages](#languages "Languages")
    * [Libraries-&-Frameworks](#libraries "Libraries & Frameworks")
* [Deployment](#deployment "Deployment")
* [Credits](#credits "Credits")


# UX

## User Goals

* Presented with clear instructions on how to play the game
* See the number of blank spaces in a word 
* See the set of letters which they have already guessed
* Know when they guessed a letter correctly/incorrectly 
* Score feedback at the end of the game
* Access the leaderboard 

## User Stories

* As a user, I want to create a username that can be entered on the leaderboard
* As a user, I want to be able to read the rules of the game
* As a user, I want to be able to navigate throgu the game intuitively 
* As a user, I want to see my score at the end of the game
* As a user, I want a clear image and message to highlight if I won or lost the game
* As a user, I want to see what the final word is regardless of whether I win/loose
* As a user, I want my score to be added to the leaderboard when I finish a game 
* As a user, I want to be able to see the top results on the leaderboard 

## Site Owner Goals

* Use colour to highlight key text and when the user is required to enter a value 
* Present users with the score of their game
* Validate the user's response to ensure that they can play the game without an error 
* Capture each user's results on a leaderboard 

## User Requirements and Expectations

### Requirements

* Terminal centre of the screen 
* Clear instructions are printed on the terminal when the user starts the game. If the user restarts the game, the rules are not re-printed to the terminal 
* The score displayed at the end of the game 
* The result (win/loss) is displayed at the end of a round 
* Game validation: 
    * The selected word must not have any spaces or dashes (-)
    * The user cannot enter the same letter multiple times 
    * The user can only enter letters and no other keys 
    * All unguessed letters are replaced with a "_." 
    * A complete word guess must have the same number of letters as the answer word 
    * If the user runs out of lives, the game ends 

## Expectations

* I expect to know how many lives I have remaining 
* I expect the letters of the answer word to be hidden by a "_" 
* I expect to know when the game starts and finishes
* I expect to be able to access the leaderboard before starting a game and after a game finishes 
* I expect to see an image dictating whether I won or lost at the end of the game 
* I expect feedback on performance

## How to Play

* A random word is selected from a file with 5000 
* Each letter is replaced with a _
* Once the user guesses a correct letter, it is displayed in the word 
* The user starts with seven lives 
* For Every incorrect guess, one life is deducted 
* The user can guess the complete word at any time, but the word they guess must have the same number of letters as the answer word 
* The game ends when the user either:
    * Runs out of lives 
    * Guesses all the letters in the word with lives remaining 
* The user will receive 10 points for each live remaining and bonuses for the following;
    * Guessing the complete word 25
    * Finishing the game with more than four lives remaining, 50 
    * Completing the game without losing a single word 100 

## Design Choices

### Fonts
Code Institute created the terminal, and the default font was monospace. 

### Colours

I used the colormera library to print text in several colours to highlight different purposes. The following colours were used:
* Yellow
* Green
* Red
* Cyan 

The colour of the button and  the background colour of the screen was set to the following colours – this was to create a theme that replicated an old computer game:
* Black – Background 
* Green – button 

## Images

I used patorjk.com with the font set to Big to create giant text that would appear as an image for the logo at when the program is started, to present the rules, and at the end of the game to show the result 

## Process Map 

[Process Map](/documents/process%20maps/hangman_game.pdf "Process Map")

## Features

### Existing Features

#### Start game button 

The start game button resets the terminal and the game for the user. The button is very simple and only has an hover and active state. These states give the impression that the buttons moves when the user hovers and clicks on the button. This makes it clear when the button has been clicked by the user. 

default:

![default start game button](/documents/images/start_game_button_default.png)


#### Game logo

The game logo was created using ASCII art and is highlighted in green using the Colorama library 
Welcome Message

The first time the game is run a welcome message is printed, this introduces the user to hangman and sets the theme of the messages to the user. If the user decides to replay the game after a round finishes the welcome message is not re-printed to the terminal.

![game logo](/documents/images/game_logo.png)

#### Game rules

The first time the game runs in the terminal the rules are printed before the user can select if they want to play the game or view the leaderboard. The game rules are contained within a box that I created using ASCII art.

![rules](/documents/images/rules.png)

#### Enter username

After the rules are printed the user is asked to enter a username. Validation is applied on the username to check that only letters are entered, and that the username is longer then one character. 

![default start game button](/documents/images/username.png)

#### Hidden word

When the game starts a random word is chosen and all of the letters which the user has not guessed are replaced by an underscore (_). The letters are displayed in the word only after the user enters a correct guess. 

The users input is validated to check that the value entered is a letter and that the value enterered is exactly one characted. 

The user can guess the whole word but the number of chracters they input must be equal to the number of letters in the word they are attempting to guess 
Used letters/Words

Once the user inputs a letter or a word they will be added to set. Each time the user enters an input these two sets will be checked. If the user tries to input a letter/word that is already in this set then they will receive an error message: 

![hidden words](/documents/images/hidden_letters.png)

#### Lives remaining 

Every time the user inputs a letter that is not in the word they are attempting to guess the lives counter will be reduced by 1. 

Validation is applied to ensure that the user has at least 1 life remaining. As soon as the users lives equal zero the game ends. 

Further validation is also applied to determine the colour of the statements which tells the user how many lives they have remaining: 
* Green:
![green response](/documents/images/lives_remaining_green.png)

* Yellow:
![yellow response](/documents/images/lives_remaining_yellow.png)

* Red:
![red response](/documents/images/lives_remaining_red.png)


#### Response to correct/incorrect words 

If the user enters a letter which is not in the selected letter set but is in the correct letters set a success message will be printed in green

![correct guess](/documents/images/correct_guess.png)

However, if the user enters a letter which is not in the selected letters or the correct letters set a message will be printed in red  

![incorrect guess](/documents/images/incorrect_guess.png)

#### Score

At the end of the game the users score will be printed with a feedback message depending on how many lives they have remaining. 

The user can receive scores for the following:
1.	10 points – per life remaining 
2.	25 points – for guessing the full word
3.	50 points – if more than 4 lives remain
4.	100 points – if no lives were lost 

![score at end of game](/documents/images/score.png)

#### Result 

ASCII art was used to create a result message that is printed depending on whether or not the user had any lives remaining at the end of the game
Leaderboard 

Once the game ends the users username, score and the current date are added to the google sheet in a new row. 

Victory Result:

![victory result message](/documents/images/victory_result.png)

Loss Result:

![loss result message](/documents/images/loss_result.png)

If the user chooses to display the leader board the following message prints to the terminal while the top 15 results are pulled from the google sheet 
ASCII art was used to create the leaderboard header and the colorama library was used to give it colour 

The leaderboard display function will print max 15 rows but if there are less then 15 rows this function will count the number of populated rows and print only this number of rows to the terminal

![display leaderboard](/documents/images/leaderboard.png)

#### Play Again

When the user finishes the game or if the user is viewing the leaderboard they will be presented with either 3 or 2 options respectively 

Options at the start of the game:

![start game options](/documents/images/start_game_options.png)

Options when viewing the leaderboard:

![leaderboard options](/documents/images/leaderboard_options.png)

#### Leaderboard 

If the user chooses to play the game the game will restart from when the user has to enter a username 

![display leaderboard](/documents/images/leaderboard.png)

### Features to be implemented 

#### Different levels of difficulty 

In the future I would like to include an option to play the game in three different difficulty levels and each level will determine the range of letters in the word and the number of lives the user has to guess the word 

For example, an easy level could have words with between 3-5 words and the user has 7 lives but a hard level would see the user guess words with 7+ letters with only 5 lives. 

## Testing

### Code Validation 

Using Code Institutes Python Linter validator, I have identified several errors of trailing whitespace. 

Error Messages:

![welcome message bug](/documents/images/pep8_code_validation.png)


### contrast checking 

![contrast checker result](/documents/images/contrast_checker.png)

## Resolved Bugs 

### If statement with break and continue to skip the intro message

When the intro message is printed the user can enter text to the terminal as the message is printed out. This is a poor user experience as an intuitive and expected response would be for the program to skip the intro text. 

Result when user inputs keys during the intro messaging being printed 

![welcome message bug](/documents/images/bug_welcome_message.png)
 
Expected result 

![welcome message bug expected result](/documents/images/welcome_message_expected_result.png)
 
### Enter A) To Play or B) To view the leaderboard:

If the user enters B at this point then the program prints the message “display leaderboard” but the expectation is that the leaderboard data is displayed:  

![view leaderboard bug](/documents/images/bug_call_leaderboard.png)

### Enter button must be an accepted key for the press about 

After the intro text is printed, the user is asked to enter any key to continue with the game. However, if the user presses the Enter button, then the validation check will fail, and the message will be printed again. 

![enter button bug bug](/documents/images/bug_enter_button_does_not_start_game.png)
 
### If you enter a letter that was already entered, then change the response message 

If the user selects a word that was already guessed the previous success/incorrect message will be printed. This will give the user 

In the following message A was entered and an incorrect message was printed but then A was entered for a second time and the same error message was printed again:

![input response message bug](/documents/images/bug_response_message.png)
 
### Full Word Not Printed 

When you completed the game with a win or loose message the final word is not printed, so the user does not see the word they were trying to guess. 

This leads to poor user experience.

![end game result bug](/documents/images/bug_lost_message.png)

### Application terminates when a user enters an invalid or empty response to the when asked to select A or B to proceed 

If the user enters any value other then A or B they will be presented with an error message and askebug_invalid_responsee response until a valid response is entered 

![Invalid response bug](/documents/images/bug_invalid_response.png)

### Application terminates when a user enters an empty response when prompted to enter their name

If the user enters a blank response when promoted to enter a username they will now be presented with an error message and asked to retype there response until a valid response is entered 

![Invalid username response bug](/documents/images/bug_user_name_invalid_response.png)

### If a user guesses all the correct letters there is no indication that they've won and the game does not end 

When the user wins the game the win game result method is correctly called and the winning message, score and final word is dispalyed 

![Invalid username response bug](/documents/images/bug_winning_result.png)

### Guessing the correct word will result in the application terminating 

When the user guesses a word it is correctly added to the guessed words list and if it is correct the winning result will be displayed 

Winning Message:
![Invalid username response bug](/documents/images/bug_winning_result.png)

Guessed Word List:
![Invalid username response bug](/documents/images/bug_guess_word.png)


### If the user presses a button before pressing enter to start the game the system crashs 

No result happens except for when the users presses the enter button as requested 
 
## Technologies used

### Languages
* HTML for the structure of the site
* CSS for the design of the site
* JavaScript was built into the template supplied by Code Institute
* Python for the game code
* Markdown for the content in my README file

### Libraries and Frameworks

* Python package for Google Sheets gspread
* Colorama 
* Time
* Sys
* Random
* String
* Datetime
* For delaying the appearance of the text python time library
* For selecting a random card from the deck python random library

### Tools

* Gitpod
* Code Institute Python Linter validator 
* WebAIM contrast checking
* For the colour pallet Colourmind
* For spell checking Grammarly
* For google drive and google sheet APIs Google Cloud Platform
* To hold the completed game data Google Sheets
* Stackoverflow for general queries

### Deployment

1. Log in/create an account on Heroku .
2. Click the button New from the dashboard in the top right corner and select Create New App on the drop-down menu .
3. You must enter a unique app name, (I used orans-hangman).
4. Then select your region I chose Europe.
5. After select the Create App button.
6. After this you will see the the project’s Deploy Tab. Open the Settings Tab and scroll down to Config Vars.
7. Click Reveal Config Vars and enter port into the Key box and 8000 into the Value box and click the Add button.
8. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes.
9. Repeat step 8 to add node.js. Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order.
10. Scroll to the top of the page and now choose the Deploy tab.
11. Select Github as the deployment method.
12. Confirm you want to connect to GitHub. 8 Search for the repository name and click the connect button.
13. Scroll to the bottom of the deploy page and select preferred deployment type:
14. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github.
15. Select the correct branch for deployment from the drop-down menu and click Deploy Branch for manual deployment.

### Credits

* Code Institute 
* Simen Daehlin 
* Youtube Channel: Kite
* Youtube Channel: Kylie Ying
