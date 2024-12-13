# ITP 115, Fall 2023
# Assignment 7
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870
# Description: Rock, paper, scissors game where user plays computer

import random

def displayRules():
    # prints out the rules
    print("The rules of Rock Paper Scissors are:")
    print("   rock smashes scissors")
    print("   scissors cut paper")
    print("   paper covers rock")
    print("   If both hands are the same, it is a tie")

def getUserHand(optionsList):
    print("The options are", optionsList)
    wrong = True
    userchoice = ""
    # checks if the user input was in the list after making it lowercase
    # and stripping white space
    while wrong == True:
        userchoice = input("Enter choice: ")
        userchoice = userchoice.lower()
        userchoice = userchoice.strip()
        for num in range(len(optionsList)):
            if userchoice == optionsList[num]:
                # breaks loop if a match
                wrong = False
                break
    print("User plays", userchoice)
    # returns the choice and prints it out
    return userchoice

def getComputerHand(optionsList):
    # gets a random hand for the computer
    randnum = random.randint(0, len(optionsList) - 1)
    computerhand = optionsList[randnum]
    print("Computer plays", computerhand)
    # returns hand and prints it out
    return computerhand

def getGameResult(userStr, computerStr):
    # this is just the game theory and finds out who wins
    if userStr == computerStr:
        print("You and the computer tied.")
        return "tie"
    if userStr == "rock" and computerStr == "paper":
        print("Computer wins.")
        return "computer"
    if userStr == "rock" and computerStr == "scissors":
        print("You win!")
        return "user"
    if userStr == "paper" and computerStr == "scissors":
        print("Computer wins.")
        return "computer"
    if userStr == "paper" and computerStr == "rock":
        print("You win!")
        return "user"
    if userStr == "scissors" and computerStr == "rock":
        print("Computer wins.")
        return "computer"
    if userStr == "scissors" and computerStr == "paper":
        print("You win!")
        return "user"

def main():
    options = ["rock", "paper", "scissors"]
    computerc = 0
    userc = 0
    displayRules()
    # after displaying rules it plays the game up until the first person reaches 2
    while computerc != 2 and userc != 2:
        userhand = getUserHand(options)
        computerhand = getComputerHand(options)
        outcome = getGameResult(userhand, computerhand)
        print("")
        # adds one based on who wins
        if outcome == "computer":
            computerc += 1
        if outcome == "user":
            userc += 1
    if computerc == 2:
        print("Computer won 2 games.")
    if userc == 2:
        print("You won 2 games!")
# calls main
main()








