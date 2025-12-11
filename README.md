# word_guessing_game

Similar to previous project of guessing a number here we will be guessing a word

It is a simple word-guessing game where the user has to guess the characters in a randomly selected word within a limited number of attempts. The program provides feedback after each guess, helping the user to either complete the word or lose the game based on their guesses.

## Algorithm

1. inporting random module of python
2. list of possible words will be created and a random word will be choosen
3. program prompts the user to start guessing the characters of the randomly chosen word
4. Initializing Guesses and Turns
    -> guesses: An empty string that will hold all the characters guessed by the user
    -> turns: The number of attempts the user has to guess the word. 
5. This while loop will run as long as the user has remaining turns. Inside the loop, the user will be prompted to guess characters.
    -> A counter for the number of characters that have not been correctly guessed will be intialized to 0
    -> The for loop iterates through each character in the word
    -> If the character has been guessed (i.e., it is in guesses), it will be displayed. If the character has not been guessed, an underscore (_) is displayed, and counter will be incremented.
6. if the counter == 0 then the user wins the game
7. else the user will be asked to guess another character and that character will be concatenated with the guesses string we intialized earlier
8. if the guessed character not in words then number of turns decreases by 1, a wrong message will be displayed along with the number of turns left
9. if turns == 0 then the user has lost 

## Problems 

Even though the player will be surprised by every word after some point he will become better at it as there are only limited words

## Solution

Lets take the word from online websites itself so that every time someone playes the game the new word genrates

Lets import requests as well and get Randon Word APIs 