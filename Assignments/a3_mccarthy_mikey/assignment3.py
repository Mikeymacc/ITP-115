# ITP 115, Fall 2023
# Assignment 3
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870
# Description: program takes user input of food and how muc h money they have and gives back change

# prints options
print("Select a food item:")
print("a) Aero Chocolate Bar for $1.95")
print("b) Beaver Tail Pastry for $7.25")
print("c) Coffee Crisp for $2.40")
print("d) Dill Pickle Chips for $4.35")
userc = input("Choice: ")
cost = 0
name = ""
# gets user decision
if userc == 'a' or userc == 'A':
    cost = 195
    name = "Aero Chocolate Bar"
elif userc == 'b' or userc == 'B':
    cost = 725
    name = "Beaver Tail Pastry"
elif userc == 'c' or userc == 'C':
    cost = 240
    name = "Coffee Crisp"
elif userc == 'd' or userc == 'D':
    cost = 435
    name = "Dill Pickle Chips"
else:
    print("You entered an invalid choice.")
    print("The item selected is Aero Chocolate Bar")
    cost = 195
    name = "Aero Chocolate Bar"
# gets the users payment
print("Payment time!")
toonies = int(input("# of toonies: "))
loonies = int(input("# of loonies: "))
quarters = int(input("# of quarters: "))
nickels = int(input("# of nickels: "))
total = (toonies * 200) + (loonies * 100) + (quarters * 25)  + (nickels * 5)

print("Cost is", cost, "cents")
print("Payment is", total, "cents")
change = total - cost
if cost > total:
    print("You did not pay enough money and will not receive the", name)
else:
    print("You purchased the", name)

    print("Your change is", change, "cents")
# gets the change
tooniechange = change // 200
change %= 200
looniechange = change // 100
change %= 100
quarterchange = change // 25
change %= 25
nickelchange = change // 5
change %= 5

# gets the change and returns it
print("Coins returned")
print("# of toonies is", tooniechange)
print("# of loonies is", looniechange)
print("# of quarters is", quarterchange)
print("# of nickels is", nickelchange)



