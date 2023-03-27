import random

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        if guess.lower() in self.word:
            print(f"Good guess! {guess} is in the word.")
    
    def ask_for_input(self):
        while True:
            guess = input("Please enter a letter")
            if len(guess) != 1 or guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
            self.list_of_guesses.append(guess)
            break


fruit_list = ["kiwi", "passion fruit", "peach", "pineapple", "mango"]
fruit_game = Hangman(fruit_list)
fruit_game.ask_for_input()





