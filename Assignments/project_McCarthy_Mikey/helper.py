# ITP 115, Fall 2023
# Final Project
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section: 31870
# Filename: helper.py
# Description: This folder contains several helper functions that mostly just aid in the creation of other functions in
# user_io. However, most importantly, it creates the data list that we will be using

def createDataList(csvFileStr = "computer_languages.csv"):
    # creates blank list of dictionaries then opens the given file
    listOfDicts = []
    fileIn = open(csvFileStr, "r")
    # gets the headers that are at the top of the csv file and makes them into a list
    header = fileIn.readline()
    header = header.strip()
    headerList = header.split(",")
    # goes through each line of the file after the header line
    for line in fileIn:
        # creates a blank dictionary
        aLanguagedict = {}
        # cleans and splices up the data into a list
        line = line.strip()
        dataList = line.split(",")
        # loops through the length of each line
        for counter in range(len(headerList)):
            # sets key equal to corresponding header index
            key = headerList[counter]
            # sets the actual value to the corresponding data
            value = dataList[counter]
            # then adds the key with its value to the dictionary
            aLanguagedict[key] = value
        # after each dictionary is made, it is added to the list
        listOfDicts.append(aLanguagedict)

    # close the file and return the list
    fileIn.close()
    return listOfDicts


def getUniqueValues(dataList, keyStr):
    # creates empty list
    unique = []
    # goes through the given data list
    for lang in dataList:
        # gets the data that matches the key
        value = lang.get(keyStr, "")
        # if the value is not in the unique list, it adds it
        if value not in unique:
            unique.append(value)
    # after creating the list, it is sorted then returned
    unique.sort()
    return unique

def largestValue(dataList, keyStr):
    # sets the largest language to the first in the list
    # and the largest value to 0
    largestlanguage = dataList[0]
    largestvalue = 0
    # goes through the data list
    for language in dataList:
        # gets the correct key and makes sure it's a digit
        valuestr = language.get(keyStr, "NA")
        if valuestr.isdigit():
            # turns it into a int so it can be compared
            value = int(valuestr)
            # if it is larger, then you change the 'large' values
            if value > largestvalue:
                largestvalue = value
                largestlanguage = language
    # after looping through everything, the largest language is returned
    return largestlanguage


def smallestValue(dataList, keyStr):
    # sets the smallest language to the first in the list
    # and the smallest value to 0
    smallestlanguage = dataList[0]
    smallestvalue = 99999999999999999
    # goes through the data list
    for language in dataList:
        valuestr = language.get(keyStr, "NA")
        # gets the correct key and makes sure it's a digit
        if valuestr.isdigit():
            # turns it into a int so it can be compared
            value = int(valuestr)
            # if it is smaller, then you change the 'small' values
            if value < smallestvalue:
                smallestvalue = value
                smallestlanguage = language
    # after looping through everything, the smallest language is returned
    return smallestlanguage


