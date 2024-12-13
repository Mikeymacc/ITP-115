#ITP 115, Fall 2023
# Lab 6
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870

import random


def displayRectangle(width, height, symbol = "#"):
    for num in range(height):
        print(symbol * width)


def main():
    print("Display Rectangles")
    randheight = random.randint(1, 10)
    randwidth = random.randint(1, 10)
    print("Random width =", randwidth)
    print("Random height =", randheight)
    displayRectangle(randwidth, randheight)
    inrange = False
    while inrange == False:
        inwidth = int(input("Enter a width (1-10): "))
        inheight = int(input("Enter a width (1-10): "))
        if(inwidth >= 1 and inwidth <= 10 and inheight >= 1 and inheight <= 10):
            inrange = True
        insymbol = input("Enter a symbol: ")
    displayRectangle(inwidth, inheight, insymbol[0])
main()




