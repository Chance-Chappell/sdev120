# Program: Even or Odd Number Checker
# Author: Chance Chappell
# Date: 4-17-26
# Description: This program asks the user to enter 15 numbers,
# stores them in a list, and determines whether each number is even or odd.

# Create an empty list to store numbers
numbers = []

# Loop to collect 15 numbers from the user
for i in range(15):
    num = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(num)

# Loop through the list and check each number
for number in numbers:
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
