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
            for count, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[count] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    
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

fruit_list = ["kiwi", "passionfruit", "peach", "pineapple", "mango"]

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            break

play_game(fruit_list)

