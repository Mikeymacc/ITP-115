# ITP 115, Fall 2023
# Assignment 5
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870
# Description: Allows user to play a game using a virtual 20-sided die and
# the user selects cases to win points

import random
score = 0
for num in range(5):
    casenum = 0
    while casenum < 1 or casenum > 5:
        casenum = int(input("Enter a number (1-5): "))

    print("You are playing Case", casenum)
    print("To win, roll one of the following numbers")

    if casenum == 1:
        validnum = list(range(2, 21, 2))
    elif casenum == 2:
        validnum = list(range(1, 20, 2))
    elif casenum == 3:
        validnum = list(range(5, 11))
    elif casenum == 4:
        validnum = list(range(10, 21, 2))
    elif casenum == 5:
        validnum = list(range(3, 20, 3))

    for nums in validnum:
        print(nums, end = "  ")

    print(" ")
    print(" ")

    randroll = random.randint(1, 20)
    print("You rolled a", randroll)

    if randroll in validnum:
        print("You win 50 points!")
        score += 50
    else:
        print("You didn't win.")
    print("")

print("Your total score is", score, "points.")


