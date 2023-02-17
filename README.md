# G*al F*r This Pr*ject 

This Pr*ject will be a text-based pyth*n game where the user guesses the letters that make up a w*rd bef*re their lives run *ut. T* win the game, the user must guess all the letters bef*re they run *ut *f lives. The user receives a sc*re based *n them guessing the w*rd c*rrectly and the number *f lives they have remaining. There are b*nus sc*res f*r guessing the w*rd with*ut l*sing a single life *r if the user has m*re than f*ur lives remaining. The user must try t* finish the game with the highest sc*re p*ssible. 

![G*als f*r this pr*ject image]()


# Table *f C*ntens 

* [UX](#ux "UX")
    * [User G*als](#user-g*als "User G*als")
    * [User St*ries](#user-st*ries "User St*ries")
    * [Site *wner G*als](#site-*wner-g*als "Site *wner G*als")
* [Requirements and Expectati*ns](#requirements-and-expectati*ns "Requirements and Expectati*ns")
    * [Requirements](#Requirments "Requirements")
    * [Expectati*ns](#expectati*ns "Expectati*ns")
    * [H*w-T*-Play](#h*w-t*-play "H*w T* Play")
* [Design-Ch*ices](#design-ch*ices "Design Ch*ices")
    * [F*nts](#f*nts "F*nts")
    * [C*l*urs](#c*l*urs "C*l*rs")
    * [Pr*cess](#pr*cess "Pr*cess")
* [Features](#features "Features")
    * [Existing-Features](#existing-features "Existing Feautres")
        * [Start-Game-Butt*n](#start-game-butt*n "Start Game Butt*n")
        * [Game-L*g*](#game-l*g* "Game L*g*")
        * [Welc*me-Message](#welc*me-message "Welc*me Message")
        * [Game-Rules](#game-rules "Game Rules")
        * [Enter-Username](#enter-username "Enter Username")
        * [Hidden-Letters](#hidden-letters "Hidden Letters")
        * [User-Letters/W*rds](#used-letters/w*rds "User Letters and W*rds")
        * [Lives Remaining](#lives-remaining "Lives Remaining")
        * [Resp*nse-T*-C*rrect/Inc*rrect-Letters](#resp*nse-t*-c*rrect/inc*rrect-letters "Resp*nse T* C*rrect/Inc*rrect Letters")
        * [Sc*re](#sc*re "Sc*re")
        * [Result](#result "Result")
        * [Leaderb*ard](#leaderb*ard "Leaderb*ard")
    * [Features-T*-Be-Implemented](#features-t*-be-implemented "Features t* be Implemented")
        * [Difficulty-Levels](#difficulty-levels "Difficulty Levels")
* [Testing](#testng "Testing")
    * [UAT](#uat "UAT")
    * [C*de-Validati*n](#c*de-validati*n "C*de Validati*n")
    * [C*ntrast-Testing](#c*ntrast-testing "C*ntrast Testing")
    * [Res*lve-Bugs](#res*lved-bugs "Res*l*ved Bugs")
    * [*pen-Bugs](#*pen-bugs "*pen Bugs")
* [Techn*l*gies](#techn*l*gies "Techn*l*gies")
    * [Languages](#languages "Languages")
    * [Libraries-&-Framew*rks](#libraries "Libraries & Framew*rks")
* [Depl*yment](#depl*yment "Depl*yment")
* [Credits](#credits "Credits")


# UX

## User G*als

* Presented with clear instructi*ns *n h*w t* play the game
* See the number *f blank spaces in a w*rd 
* See the set *f letters which they have already guessed
* Kn*w when they guessed a letter c*rrectly/inc*rrectly 
* Sc*re feedback at the end *f the game
* Access the leaderb*ard 

## User St*ries

* As a user, I want t* create a username that can be entered *n the leaderb*ard
* As a user, I want t* be able t* read the rules *f the game
* As a user, I want t* be able t* navigate thr*gu the game intuitively 
* As a user, I want t* see my sc*re at the end *f the game
* As a user, I want a clear image and message t* highlight if I w*n *r l*st the game
* As a user, I want t* see what the final w*rd is regardless *f whether I win/l**se
* As a user, I want my sc*re t* be added t* the leaderb*ard when I finish a game 
* As a user, I want t* be able t* see the t*p results *n the leaderb*ard 

## Site *wners G*als

* Use c*l*ur t* highlight key text and when the user is required t* enter a value 
* Present users with the sc*re *f their game
* Validate the user's resp*nse t* ensure that they can play the game with*ut an err*r 
* Capture each user's results *n a leaderb*ard 

## User Requirements and Expectati*ns

### Requirements

* Terminal centre *f the screen 
* Clear instructi*ns are printed *n the terminal when the user starts the game. If the user restarts the game, the rules are n*t re-printed t* the terminal 
* The sc*re displayed at the end *f the game 
* The result (win/l*ss) is displayed at the end *f a r*und 
* Game validation: 
    * The selected w*rd must n*t have any spaces *r dashes (-)
    * The user cann*t enter the same letter multiple times 
    * The user can *nly enter letters and n* *ther keys 
    * All unguessed letters are replaced with a "_." 
    * A c*mplete w*rd guess must have the same number *f letters as the answer w*rd 
    * If the user runs *ut *f lives, the game ends 

## Expectations

* I expect to know how many lives I have remaining 
* I expect the letters of the answer word to be hidden by a "_" 
* I expect to know when the game starts and finishes
* I expect to be able to access the leaderboard before starting a game and after a game finishes 
* I expect to see an image dictating whether I won or lost at the end of the game 
* I expect feedback on performance

## How to Play

*	A random word is selected from a file with 5000 
*	Each letter is replaced with a _
*	Once the user guesses a correct letter, it is displayed in the word 
*	The user starts with seven lives 
*	For Every incorrect guess, one life is deducted 
*	The user can guess the complete word at any time, but the word they guess must have the same number of letters as the answer word 
*	The game ends when the user either:
    * Runs out of lives 
    * Guesses all the letters in the word with lives remaining 
*	The user will receive 10 points for each live remaining and bonuses for the following;
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

## Features

### Existing Features

#### Start game button 

The start game button resets the terminal and the game for the user. The button is very simple and only has an hover and active state. These states give the impression that the buttons moves when the user hovers and clicks on the button. This makes it clear when the button has been clicked by the user. 

Static:

On-hover:

Active:

#### Game logo

The game logo was created using ASCII art and is highlighted in green using the Colorama library 
Welcome Message
The first time the game is run a welcome message is printed, this introduces the user to hangman and sets the theme of the messages to the user. If the user decides to replay the game after a round finishes the welcome message is not re-printed to the terminal. 

#### Game rules

The first time the game runs in the terminal the rules are printed before the user can select if they want to play the game or view the leaderboard. The game rules are contained within a box that I created using ASCII art.

#### Enter username

After the rules are printed the user is asked to enter a username. Validation is applied on the username to check that only letters are entered, and that the username is longer then one character. 

#### Hidden word

When the game starts a random word is chosen and all of the letters which the user has not guessed are replaced by an underscore (_). The letters are displayed in the word only after the user enters a correct guess. 

The users input is validated to check that the value entered is a letter and that the value enterered is exactly one characted. 

The user can guess the whole word but the number of chracters they input must be equal to the number of letters in the word they are attempting to guess 
Used letters/Words

Once the user inputs a letter or a word they will be added to set. Each time the user enters an input these two sets will be checked. If the user tries to input a letter/word that is already in this set then they will receive an error message: 

#### Lives remaining 

Every time the user inputs a letter that is not in the word they are attempting to guess the lives counter will be reduced by 1. 

Validation is applied to ensure that the user has at least 1 life remaining. As soon as the users lives equal zero the game ends. 

Further validation is also applied to determine the colour of the statements which tells the user how many lives they have remaining: 
* Green:
* Yellow:
* Red:

#### Response to correct/incorrect words 

If the user enters a letter which is not in the selected letter set but is in the correct letters set a success message will be printed in green
However, if the user enters a letter which is not in the selected letters or the correct letters set a message will be printed in red  

#### Score

At the end of the game the users score will be printed with a feedback message depending on how many lives they have remaining. 

The user can receive scores for the following:
1.	10 points – per life remaining 
2.	25 points – for guessing the full word
3.	50 points – if more than 4 lives remain
4.	100 points – if no lives were lost 

#### Result 

ASCII art was used to create a result message that is printed depending on whether or not the user had any lives remaining at the end of the game
Leaderboard 

Once the game ends the users username, score and the current date are added to the google sheet in a new row. 

If the user chooses to display the leader board the following message prints to the terminal while the top 15 results are pulled from the google sheet 
ASCII art was used to create the leaderboard header and the colorama library was used to give it colour 

The leaderboard display function will print max 15 rows but if there are less then 15 rows this function will count the number of populated rows and print only this number of rows to the terminal

#### Play Again

When the user finishes the game or if the user is viewing the leaderboard they will be presented with either 3 or 2 options respectively 
Game Finish

#### Leaderboard 

If the user chooses to play the game the game will restart from when the user has to enter a username 
