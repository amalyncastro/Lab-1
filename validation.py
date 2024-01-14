# Lab 1, DNA validation
# Program Author: Amalyn Castro
# Creation Date: 1/14
# This program determines whether the string entered by the user is a valid DNA sequence 
# (strings that only contian the characters "A", "T" "C", "G," and "-") However, if there 
# is an empty string or invalid characters it will state that the statement is not a valid 
# DNA sequence

# valid characters
valid = {"A", "T", "C", "G", "-"}
# not valid characters
not_valid = ""

# asks for a DNA sequence and stores it into seq1
seq = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")

# if any of the characters in seq are not variables in valid or are in not_valid, print that seq is not a valid DNA sequence
if any(char not in valid for char in seq) or seq == not_valid:
    print(f"{seq} is not a valid DNA sequence")
# else, if any of the characters in seq are variables in valid, print that seq is a valid DNA sequence
else:
    print(f"{seq} is a valid DNA sequence")