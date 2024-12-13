#ITP 115, Fall 2023
# Lab 9
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870

def readFile(fileName):
    returnDict = {}
    fileIn = open(fileName, "r")

    for line in fileIn:
        line = line.strip()
        wordsList = line.split()
        for word in wordsList:
            word = word.lower()
            word = word.strip(",.?:")
            if word in returnDict:
                returnDict[word] = returnDict[word] + 1
            else:
                returnDict[word] = 1

    fileIn.close()
    return returnDict

def sortKeys(dictionary):
    specialList = dictionary.keys()
    regularList = list(specialList)
    regularList.sort()
    return regularList

def main():
    dictionary = readFile("lab9_poem.txt")
    wordList = sortKeys(dictionary)
    print("Words and their number of occurrences: ")
    for item in wordList:
        print(item, "->", dictionary[item])
main()


