import random

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        word = random.choice(self.word_list)
        word_guessed = []
        num_letters = 
        list_of_guesses = []
