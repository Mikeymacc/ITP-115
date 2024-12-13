# ITP 115, Fall 2023
# Assignment 8
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870
# Description: number guessing game where the user guesses
# a random number list


import random

def isSingleDigit(userStr):
    # checks if the input is a single digit
    if len(userStr) == 1 and userStr.isdigit() == True:
        return True
    else:
        return False

def createCodeList(num):
    # creates the random list by adding the random numbers to a list
    list = []
    for i in range(num):
        list.append(random.randint(0, 9))
    return list

def createUserList(num):
    # lets the user guess the digits in random list and makes sure the guesses are single digits
    print("The number of digits in the code is", num)
    list2 = []
    for i in range(num):
        usernum = input("Enter a digit at index " + str(i) + ": ")
        while isSingleDigit(usernum) == False:
            usernum = input("Enter a digit at index " + str(i) + ": ")

        list2.append(int(usernum))
    print("Your guess is", list2)
    return list2

def displayHints(codeList, userList, num):
    # displays hints based on what numbers you have gotten right and if they are in the right placement
    print("Generating hints...")
    hints = 0
    for i in range(num):
        if codeList[i] == userList[i]:
            print("index", i, "->", userList[i], "is correct")
            hints+=1
        count = codeList.count(userList[i])
        if count > 0:
            print("index", i, "->", userList[i], "occurs", count, "time(s)")
            hints += 1
    if hints == 0:
        print("No correct digits")


def main():
    # the main function that goes until the user cracks the code and then tells you how many guesses it took
    numval = 3
    codelist = createCodeList(numval)
    userlist = createUserList(numval)
    guess = 1
    while codelist != userlist:
        print("")
        displayHints(codelist, userlist, numval)
        print("")
        userlist = createUserList(numval)
        guess +=1
    print("You cracked the code in", guess, "guesses!")
main()




