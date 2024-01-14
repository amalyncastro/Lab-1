# Lab 1, Complete program
# Program Author: Amalyn Castro
# Creation Date: 1/14
# This program puts the pieces together and composes a sequence alignment program. This program only completes scoring if valid DNA sequences are entere

# valid characters
valid = {"A", "T", "C", "G", "-"}
# not valid characters
not_valid = ""

# print a greeting message
print("Hello and welcome to DNA sequence alignment program!")
seq1 = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): \n")
seq2 = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")
print(f"\nYou entered:\n{seq1}\n{seq2}")

# while x != 'q', keep printing x.
while True:
    x = input("Select one of the following commands:\n'u' to update sequences\n's' to score the alignment\n'q' to quit\n")
# if x == 'q', break out of the while loop
    if x == 'q':
        break
# continue iterating through the while loop if x != 'q'
    if x == 's':
# if any of the characters in seq are not variables in valid or are in not_valid, print that seq is not a valid DNA sequence
        if any(char not in valid for char in seq1 or seq2) or seq1 == not_valid or seq2 == not_valid:
            print("Invalid DNA sequences entered, please re-enter sequences")
        else:
            matches = 0
            # a for loop that iterates from 0 to the minimum length of the two sequences
            for i in range(min(len(seq1), len(seq2))):
            # checks if the characters at the curent position i in both sequences are the same
                if seq1[i] == seq2[i]:
            # is so, matches increases by one
                    matches += 1
            # if matches is not 1, print the statement with "matches"
            if matches != 1:
                print(f"{matches} matches found between {seq1} and {seq2}")
            # else, print matches as "match"
            else:
                print(f"{matches} match found between {seq1} and {seq2}")
            
    if x == 'u':
        seq1 = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): \n")
        seq2 = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): \n")
        print(f"You entered:\n{seq1}\n{seq2}")
    else:
        continue
# print a goodbye statement
print("Thank you! Goodbye!")
