#ITP 115, Fall 2023
# Lab 8
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870

def readFile(userGenre, fileName = "lab8_csv"):
    fileIn = open(fileName, "r")
    showList = []
    for line in fileIn:
        line = line.strip()
        dataList = line.split(",")
        showName = dataList[0]
        showGenre = dataList[1]

        if userGenre == showGenre:
            showList.append(showName)

    fileIn.close()
    return showList

def writeFile(userGenre, showList):
    fileOut = open(userGenre + ".txt" , "w")
    for showName in showList:
        print(showName, file = fileOut)
    fileOut.close()

def main():
    print("TV Shows")
    genreList =  ['action', 'animation', 'comedy', 'documentary', 'drama', 'mystery',
   'scifi', 'western']
    print("Possible genres are")
    print(genreList)
    userGenre = input("Enter a genre: ")
    while userGenre not in genreList:
        userGenre = input("Enter a genre: ")

    showList = readFile(userGenre)
    writeFile(userGenre, showList)

main()