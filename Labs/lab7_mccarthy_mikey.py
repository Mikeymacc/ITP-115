#ITP 115, Fall 2023
# Lab 7
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870

import random

def getUserOption(optionsList):
    prompt = "Enter " + " or ".join(optionsList) + ": "
    userchoice = input(prompt)
    userchoice = userchoice.lower()
    while userchoice not in optionsList:
        userchoice = input(prompt)
        userchoice = userchoice.lower()
    print("User entered", userchoice)
    return userchoice

def getRandomOption(optionsList):
    choice = random.choice(optionsList)
    print("Computer selected", choice)
    return choice

def main():
    list = ["heads", "tails"]
    user = getUserOption(list)
    computer = getRandomOption(list)
    if user == computer:
        print("You matched!")
    else:
        print("No match")
main()




