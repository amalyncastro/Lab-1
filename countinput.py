# Lab 1, Count input length without spaces, periods, exclamation points, or commas
# Program Author: Amalyn Castro
# Creation Date: 1/14
# This program is given a line of text as input and outputs the numeber of characters excluding spaces, periods, exclamation points, or commas.

# x is equal to an empty input to store the statement
x = input()
# counter is set to 0 to begin counting
counter = 0
# any invalid characters will be stored in the bad variable instead
bad = ""

# checks each individual character in x
for char in x:
    # if x contains a space, period, exclamation point, or a comma, store the character in bad.
    if char == " " or char == "." or char == "!" or char == ",":
        bad += char
    # else, store the character in counter
    else:
        counter += 1

# print counter (doesn't contain any invalid characters)
print(counter)

