# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Milestone 2

The random module is imported to allow a random selection from a list.
A list of fruits is created and the random.choice() method is used to select a random fruit, which is assigned to the _word_ variable.
The user is asked to input a letter. 
A check is run to confirm the user input a single, alphabetical letter.

# Milestone 3


Two functions are created to make the code easier to read. The first function, check_guess(), ensures the guess is lower case and then checks if it is in the word. The second function, ask_for_input(), asks the user for input and iteratively checks if the guess is a valid, single alphabetical character. Once the user has entered a valid guess, the check_guess() function is then called to check if the guess is in the word. The whole game runs by calling the ask_for_input() function. 

# Milestone 4

The functionality for the game is encapsulated into a Hangman class. 

The class initializes with two parameters, the word list to be used and the number of lives left, which starts at 5. The other attributes are the word guessed so far, the number of unique letters still to guess, the word (randomly chosen from the word list), and the list of letters guessed so far. 

The class has two methods: ask_for_input, and check_guess.

The ask_for_input mthod asks the user to enter a letter, checks the input is a valid alphabetic character that has not been used before, and if so calls the check_guess method and appends the guess to the list of guesses. The function contains a while loop that stops once the number of letters left to guess is zero. 

The check_guess function chcks if the guess passed from ask_for_input is in the word. If so, it updates the progress of the word guessed so far, and reduces the number of letters left to guess. If not, it reduces the number of lives left and prints a sorry message and the remaining number of lives. 