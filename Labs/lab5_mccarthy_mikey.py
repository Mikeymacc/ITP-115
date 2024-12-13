#ITP 115, Fall 2023
# Lab 4
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870

import random

nouns = ['platypus', 'computer', 'butterfly']
verbs = ['danced', 'ate', 'frolicked']
adverbs = ['cheerfully', 'always', 'swiftly']
print("Sentence Creator")
print(" A) Display Nouns")
print(" B) Display Verbs")
print(" C) Display Adverbs")
print(" D) Display Sentence")
print(" Q) Quit")

answer = input("Enter a letter (A-D, Q): ")
answer = answer.upper()

while answer != 'Q':
    if answer == 'A':
        print("nouns: ", nouns)
    elif answer == 'B':
        print("verbs: ", verbs)
    elif answer == 'C':
        print("adverbs: ", adverbs)
    elif answer == 'D':
        randnoun = random.choice(nouns)
        randnoun = randnoun.capitalize()
        randverb = random.choice(verbs)
        randadverb = random.choice(adverbs)
        print(randnoun + " " + randverb + " " + randadverb + ".")
    else:
        print("Invalid Choice")
    answer = input("Enter a letter (A-D, Q): ")
    answer = answer.upper()