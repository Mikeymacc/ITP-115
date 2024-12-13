# ITP 115, Fall 2023
# Final Project
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section: 31870
# Filename: extra_credit.py
# Description: These are the extra credit functions that display languages with indentation and also display
# the top ten ranked languages

# must import the user functions
import user_io

def displayIndentLanguages(dataList):
    # loops through list and checks if the indentation is 'TRUE'
    # and then displays those languages
    print("The languages that require indentation are")
    for language in dataList:
        if language.get("indentation", "NA") == "TRUE":
            print("    " + language.get("id"))

def displayTopRanked(dataList):
    # sets rank equal to 0
    rank = 0
    # in a while loop until rank is greater than 9
    while rank <= 9:
        # loops through the languages in the data list
        for language in dataList:
            # if the languages rank is equal to string version of the rank now
            if language.get("rank", "NA") == str(rank):
                # it displays that language
                user_io.displayLanguage(language)
                # then adds 1 to the rank to continue the process
                rank += 1
    # after the loop ends, all top ranked languages 0-9 should be displayed in order

