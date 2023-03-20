import random

word_list = ["kiwi", "passion fruit", "peach", "pineapple", "mango"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please enter a letter")
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input")