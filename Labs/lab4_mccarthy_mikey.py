#ITP 115, Fall 2023
# Lab 4
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870

phrase = input("Enter a phrase: ")
changes = 0
print("Your new phrase is ")
for char in phrase:
    if char == 'A':
        print('4', end='')
        changes += 1
    elif char == 'E':
        print('3', end='')
        changes += 1
    elif char == 'I':
        print('1', end='')
        changes += 1
    elif char == 'i':
        print('1', end='')
        changes += 1
    elif char == 'S':
        print('$', end='')
        changes += 1
    elif char == 'T':
        print('7', end='')
        changes += 1
    elif char == '1':
        print('!', end='')
        changes += 1
    else:
        print(char, end='')
print("")
print("Changed", changes, "characters")





