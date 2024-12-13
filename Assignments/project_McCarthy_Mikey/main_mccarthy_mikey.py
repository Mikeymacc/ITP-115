# ITP 115, Fall 2023
# Final Project
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section: 31870
# Filename: main_mccarthy_mikey.py
# Description: Essentially puts all the functions together to allow the user to explore
# the huge data list of computer languages and learn more about them

# must import these files
import extra_credit
import helper
import user_io

def main():
    # gives the user a starting understanding of what is to happen
    print("Learn about computer languages")
    # creates the data list of languages
    dataList = helper.createDataList()
    # then creates the option list
    optionsList = user_io.createOptionsDict()
    userContinue = True
    # loops through until the user quits
    while userContinue:
        # displays the user options
        user_io.displayUserMenu(optionsList)
        # gets the user choice
        userChoice = user_io.getUserOption(optionsList)
        # if user chooses 'Q', it quits and skips the other options
        if userChoice == 'Q':
            userContinue = False
        else:
            # goes down and checks each. If it matches the letter, then it calls the corresponding function
            if userChoice == 'A':
                user_io.displayTypes(dataList)
            elif userChoice == 'B':
                user_io.displayNumProgLangs(dataList)
            elif userChoice == 'C':
                user_io.displayOldestLanguage(dataList)
            elif userChoice == 'D':
                user_io.displayMostJobs(dataList)
            elif userChoice == 'E':
                user_io.writeTextFile(dataList)
            elif userChoice == 'F':
                user_io.findLanguages(dataList)
            elif userChoice == 'G':
                extra_credit.displayIndentLanguages(dataList)
            elif userChoice == 'H':
                extra_credit.displayTopRanked(dataList)

main()