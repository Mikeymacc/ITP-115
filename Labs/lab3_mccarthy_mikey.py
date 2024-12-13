#ITP 115, Fall 2023
# Lab 3
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870
print("Get to know my favorite people...")
print(" A) Artist")
print(" B) Athlete")
print(" C) Author")
print(" Q) Quit")
letter = 'o'
count = 0
while letter != 'q' and letter != 'Q':
    count+=1
    letter = input("Option: ")
    if letter == 'a' or letter == "A":
        print("My favorite artist Picasso")
    elif letter == 'b' or letter == 'B':
        print("My favorite athlete is John Daly")
    elif letter == 'c' or letter == 'C':
        print("My favorite author is Rick Riordan")
    elif(letter == 'q' or letter == 'Q'):
        count-=1
    else:
        print("That option is not available.")
print("The number of messages displayed is", count)
