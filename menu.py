# Lab 1, User menu
# Program Author: Amalyn Castro
# Creation Date: 1/14
# This program repeatedly displays a menu of options to the user until they type "q". It also displays a freeting and a goodbye message after user quits

# print a greeting message
print("Hello and welcome to DNA sequence alignment program!")

# while x != 'q', keep printing x.
while True:
    x = input("Select one of the following commands:\n'u' to update sequences\n's' to score the alignment\n'q' to quit\n")
# if x == 'q', break out of the while loop
    if x == 'q':
        break
    # continue iterating through the while loop if x != 'q'
    continue
# print a goodbye statement
print("Thank you! Goodbye!")
