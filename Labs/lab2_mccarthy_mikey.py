#ITP 115, Fall 2023
# Lab 2
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870
year = int(input("Enter the year: "))
modyear = year % 12
animal = ""
if modyear == 0:
    animal = "Monkey"
elif modyear == 1:
    animal = "Rooster"
elif modyear == 2:
    animal = "Dog"
elif modyear == 3:
    animal = "Pig"
elif modyear == 4:
    animal = "Rat"
elif modyear == 5:
    animal = "Ox"
elif modyear == 6:
    animal = "Tiger"
elif modyear == 7:
    animal = "Rabbit"
elif modyear == 8:
    animal = "Dragon"
elif modyear == 9:
    animal = "Snake"
elif modyear == 10:
    animal = "Horse"
else:
    animal = "Goat"
print(year, "is the year of the", animal + ".")
