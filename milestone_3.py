while True:
    guess = input("Please enter a letter")
    if guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")