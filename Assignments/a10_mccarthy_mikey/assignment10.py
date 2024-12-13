# ITP 115, Fall 2023
# Assignment 10
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870
# Description: keeps a calendar of events an lets you make alterations

def displayChoices():
    # simply displays the options the user has
    print("Events Dictionary")
    print("   A) Add an event")
    print("   U) Update an event")
    print("   D) Delete an event")
    print("   P) Print the events")
    print("   Q) Quit")

def displayEvents(eventDict):
    # prints out the events in the dictionary
    for event in sorted(eventDict.keys()):
        print(event, "occurs on", eventDict[event])

def addEvent(eventDict):
    # gets user input
    event = input("Enter an event: ")
    event = event.title()
    # checks if it is not in the dictionary and adds it or tells you it is already in it
    if event not in eventDict:
        date = input("Enter the date: ")
        date = date.title()
        eventDict[event] = date
        print(event, "has been added to the events dictionary")
    else:
        print(event, "is already in the events dictionary")

def updateEvent(eventDict):
    # asks user for the event to update
    event = input("Enter an event: ")
    event = event.title()
    # checks if it is in the dictionary and then updates it or tells you it is not there
    if event not in eventDict:
        print(event, "is not in the events dictionary")
    else:
        date = input("Enter the date: ")
        date = date.title()
        eventDict[event] = date
        print(event, "has been updated to", date)

def deleteEvent(eventDict):
    # gets user input for event to delete
    event = input("Enter an event: ")
    event = event.title()
    # deletes event if its there and tells you if it is not
    if event in eventDict:
        del eventDict[event]
        print(event, "was deleted from the events dictionary")
    else:
        print(event, "is not in the events dictionary")

def main():
    # makes a dictionary and the displays choices/gets user input
    eventdictionary = {"Labor Day" : "September 4, 2023", "Memorial Day" : "May 29, 2023"}
    displayChoices()
    userinput = input("Choice: ").upper()
    # checks the users input and keeps going to the input is 'Q'
    while userinput != 'Q':
        if userinput == 'A':
            addEvent(eventdictionary)
        elif userinput == 'U':
            updateEvent(eventdictionary)
        elif userinput == 'D':
            deleteEvent(eventdictionary)
        elif userinput == 'P':
            displayEvents(eventdictionary)
        elif userinput != 'Q':
            print("Invalid choice")
        displayChoices()
        userinput = input("Choice: ").upper()
main()




