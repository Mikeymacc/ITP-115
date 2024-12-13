# ITP 115, Fall 2023
# Assignment 2
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870
# Description: (such as)
# This program creates variables, gets user input, and
# displays information to the user.
coderName = "Michael McCarthy"
coderAge = 20
name = input("Enter your name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter your favorite food: ")
cost = float(input("Enter cost for food: "))
age = int(input("Enter your age: "))
costtwo = cost * 2
bothage = coderAge + age
print("This code is written by", coderName)
print("Once upon a time, \"" + name + "\" and I went to the \"" + place + "\".")
print("We made a yummy lunch eating \"" + food + "\" which cost us $\'" + str(costtwo) + "\'.")
print("We met a \"" + animal + "\" who made us smile.")
print("We will all be friends for at least \'" + str(bothage) + "\' years.")