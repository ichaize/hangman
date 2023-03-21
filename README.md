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
