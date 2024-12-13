# ITP 115, Fall 2023
# Assignment 4
# Name: Mikey McCarthy
# Email: mtmccart@usc.edu
# Section:31870
# Description: this program takes in a set of numbers then tells you the smallest
# number, the count, the total, and the average

count = 0
total = 0
large = 0
print("Find the largest number")
print("Enter an integer (negative one to quit)")
num = 0
while num >= 0:
    num = int(input("> "))
    if(num >= 0):
        count += 1
        total += num
        if num > large:
            large = num
print("The largest number is", large)
print("The count is", count)
print("The total is", total)
average = total / count
print("The average is", average)
print(" ")

counts = 0
totals = 0
small = 100000
print("Find the smallest number")
print("Enter an integer (negative one to quit)")
nums = 0
while nums >= 0:
    nums = int(input("> "))
    if(nums >= 0):
        counts += 1
        totals += nums
        if nums < small:
            small = nums
print("The smallest number is", small)
print("The count is", counts)
print("The total is", totals)
averages = totals / counts
print("The average is", averages)
