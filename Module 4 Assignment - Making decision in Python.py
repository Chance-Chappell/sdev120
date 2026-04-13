# Program: Pass or Fail Checker
# Author: Chance Chappell
# Date: 4/11/2026
# Description: This program asks for a student's name and final grade,
# then determines if the student passed or failed.

# Get user input
name = input("Please enter your name: ")
grade = int(input("Please enter your final grade: "))

# Decision structure
if grade >= 60:
    print("Hello " + name + ", you passed this class")
else:
    print("Hello " + name + ", you failed this class")
