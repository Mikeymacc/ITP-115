# ITP 115, Fall 2023
# Assignment 8
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870
# Description: takes in a csv file and asks for user input to get
# needed info. Then displays info in a txt file

def createChoiceList(fileStr = "languages.csv"):
    # opens the file and gets the choices
    fileIn = open(fileStr, "r")
    header = fileIn.readline().strip()
    list = header.split(',')
    fileIn.close()
    return list
def createInfoList(choiceList, choiceStr, fileStr = "languages.csv"):
    #creates the info list by parsing through the csv
    infolist = []
    index = choiceList.index(choiceStr)
    fileIn = open(fileStr, "r")
    fileIn.readline()
    # adds data to the info list
    for line in fileIn:
        data = line.strip().split(',')
        infolist.append(data[index])
    fileIn.close()
    return infolist

def getUserChoice(choiceList):
    # gets the choice not including id and title
    validchoice = choiceList[2:]
    print("Available information about the languages include")
    print(validchoice)
    userchoice = input("Enter your choice: ").lower().strip()
    # makes sure user choice is in the list
    while userchoice not in validchoice:
        print(userchoice, "is not a valid choice")
        userchoice = input("Enter your choice: ").lower().strip()
    print("You have entered", userchoice)
    return userchoice

def writeFile(langList, infoList, choiceStr):
    # this makes the txt file based on the user choice and the input info lists
    filename = choiceStr + ".txt"
    fileOut = open(filename, "w")
    print("language -> " + choiceStr, file = fileOut)
    index = 0
    # makes sure it is not NA
    for index in range(len(infoList)):
        if infoList[index] != "NA":
            print(langList[index] + " -> " + infoList[index], file = fileOut)
    print("Information saved to", filename)
    fileOut.close()

def main():
    # creates the choice lists then the info list
    # after getting the user choice it makes a file
    choicelist = createChoiceList()
    infolist = createInfoList(choicelist, "title")
    userchoice = getUserChoice(choicelist)
    infolist2 = createInfoList(choicelist, userchoice)
    writeFile(infolist, infolist2, userchoice)

main()


