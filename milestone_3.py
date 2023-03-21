import random

word_list = ["kiwi", "passion fruit", "peach", "pineapple", "mango"]
print(word_list)

word = random.choice(word_list)
print(word)

while True:
    guess = input("Please enter a letter")
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")