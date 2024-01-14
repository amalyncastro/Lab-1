# Lab 1, Calculate match score
# Program Author: Amalyn Castro
# Creation Date: 1/14
# This program, given two DNA sequences, calculates their alignment score (i.e. how many positions inn both strings have matching characters).

# set matches to 0
matches = 0

# asks for a DNA sequence and stores it into seq1
seq1 = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")

# asks for a DNA sequence and stores it into seq2
seq2 = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")

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