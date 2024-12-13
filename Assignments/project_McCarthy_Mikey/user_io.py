# ITP 115, Fall 2023
# Final Project
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section: 31870
# Filename: user_io.py
# Description: These are going to be the user functions that let the user do whatever they may like with the data list
# it gives them many options to explore the list of computer languages

# have to import the helper functions to use them
import helper

def createOptionsDict(textFileStr = "menu_options.txt"):
    # creates empty dictionary
    optionsDict = {}
    # opens the given file
    fileIn = open(textFileStr, "r")
    # goes through each line of the file
    for line in fileIn:
        # cleans the data and splits each line into a list of two at the ':'
        line = line.strip()
        linelist = line.split(":")
        # gives the key which is the first value and makes it equal to the second value of the list to create
        # one entry of the dictionary
        optionsDict[linelist[0].strip()] = linelist[1]
    # closes the file and returns the options dictionary after looping through the txt file
    fileIn.close()
    return optionsDict

def displayUserMenu(optionsDict):
    # simply goes through the dictionary and prints out the key and its corresponding option
    for key in optionsDict:
        print(key, "->", optionsDict[key])

def getUserOption(optionsDict):
    wrong = True
    # loops to get user answer until it is in the given keys
    while wrong:
        user = input("Option: ").strip().upper()
        # if it is in the list, it makes the loop stop and returns the user option
        if user in optionsDict:
            wrong = False
            return user

def displayTypes(dataList):
    # uses helper function to get all the unique types
    unique = helper.getUniqueValues(dataList, "type")
    # gets the number of unique types then prints it out
    num = len(unique)
    print("The", num, "unique types are")
    # prints out each type
    for type in unique:
        print("   " + type)

def displayNumProgLangs(dataList):
    count = 0
    # after making count 0, goes through the data list
    for language in dataList:
        # if type is equal to programming then count adds 1
        type = language.get("type")
        if type == "programming":
            count += 1
            # prints total number of programming languages
    print("The total number of programming languages is", count)

def displayLanguage(langDict):
    # gets title and rank then prints them out
    title = langDict.get("title", "NA")
    rank = langDict.get("rank", "NA")
    print(title + " [#" + rank + "]")
    # if it has a type, it prints it out
    if langDict.get("type", "NA") != "NA":
        print("   Type is", langDict.get("type", "NA"))
    # if it has a data, it prints it out
    if langDict.get("appeared", "NA") != "NA":
        print("   First appeared in", langDict.get("appeared", "NA"))
    # if it has a creators, it prints it out
    creators = langDict.get("creators", "NA")
    if creators != "NA":
        # splits the creators and the 'and'
        creatorlist = creators.split(" and ")
        # if more than one creator, separates by a comma
        if len(creatorlist) > 2:
            creatorstr = ", ".join(creatorlist)
            print("   Created by", creatorstr)
            # if two then an 'and'
        elif len(creatorlist) == 2:
            print("   Created by", creatorlist[0], "and", creatorlist[1])
            # if one then just prints the name
        elif len(creatorlist) == 1:
            print("   Created by", creatorlist[0])
    # gets the file extensions if they are there
    if langDict.get("file_extensions", "NA") != "NA":
        print("   File Extensions are", langDict.get("file_extensions", "NA"))
    # gets the jobs if they are there and more than zero
    jobs = langDict.get("jobs", "NA")
    if jobs != "NA" and int(jobs) > 0:
        print("   Number of jobs is", jobs)
    # gets the users if they are there and more than zero
    users = langDict.get("users", "NA")
    if users != "NA" and int(users) > 0:
        print("   Number of users is", users)

def displayOldestLanguage(dataList):
    # uses the helper function to get the smallest appeared then displays that language
    oldest = helper.smallestValue(dataList, "appeared")
    displayLanguage(oldest)

def displayMostJobs(dataList):
    # uses helper function to get largets number of jobs then displays that language
    largest = helper.largestValue(dataList, "jobs")
    displayLanguage(largest)

def writeTextFile(dataList):
    # makes a file name
    filename = "mccarthy_mikey.txt"
    # opens a file with that name
    fileout = open(filename, "w")
    # loops through the data list
    for language in dataList:
        # finds the python language
        if language.get("id") == "python":
            # writes its rank to the file
            fileout.write("Python is rank #" + language.get("rank") + "\n")
    # also writes two things I enjoy about python
    fileout.write("I really enjoy working with python because of its simplicity compared to other languages \n")
    fileout.write("I enjoy python because its named after a cool snake \n")
    # prints where the info is saved to
    print("Information saved to", filename)

def findLanguages(dataList):
    # gets user to input a phrase
    user = input("Enter a phrase: ")
    # strips the phrase and makes it lowercase
    user = user.strip().lower()
    # sets languages found to 0
    found = 0
    # loops through data list
    for language in dataList:
        # if it is found in the lower case version of the id, title, or file extensions, it displays that language and
        # adds 1 to found
        if user in language.get("id").lower() or user in language.get("title").lower() or user in language.get("file_extensions").lower():
            displayLanguage(language)
            found += 1
    # if found is 0, then it tells you none were found with that phrase
    if found == 0:
        print("No languages contain", "'" + user + "'")
    # or tells you how many were found with that phrase
    else:
        print("Found", found, "languages that contain", "'" + user + "'")














