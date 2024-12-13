# ITP 115, Fall 2023
# Assignment 6
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870
# Description: program word guessing game that scrambles
# a word and lets the user guess what the word might be

import random
# i declare the lists
words = ["trojan", "program", "football", "python"]
jumblewords = ["anjort", "mraporg", "bloloaft", "tohpyn"]
hints = ["USC", "Code", "sport", "ITP115"]
print("There are 4 words in the guessing game.")

#get a random number for the list
randnum = random.randint(0, 3)

# prints the jumbled word for the user
print("A random word has been picked for you, and it has", len(words[randnum]), "letters.")
print("The jumbled version of the word is '" + jumblewords[randnum] + "'")

correct = False
count = 0
# while loop goes until the user gets it correct
while correct == False:
    guess = input("Enter your guess: ")
    # strips white space and makes the guess all lowercase
    guess = guess.strip().lower()
    # adds one to the  guess count
    count += 1
    # if they do not get it right it asks them for a hint
    # and displays jumbled word again
    if guess != words[randnum]:
        print("Your guess is incorrect")
        hint = input("Do you want a hint (y or n)? ")
        hint = hint.lower()
        # displays hint if user selects yes
        if hint == 'y':
            print("The hint is '" + hints[randnum] + "'")
        print("The jumbled word is '" + jumblewords[randnum] + "'")
        print(" ")
    # prints what the word is and amount of guesses if they get it correct
    else:
        correct = True
        print("The word is '" + words[randnum] + "'")
        print("The number of guesses is", count)








