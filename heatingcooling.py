# Lab 1, Heating and cooling days
# Program Author: Amalyn Castro
# Creation Date: 1/14
# This program asks the user for the average daily temperature and
# calculates the running totals of heating and cooling days. It then 
# prints two totals, Heating days (if the temperature if above 80F) and 
# Cooling Days (if the temperature is below 60F). The end of the input is 
# denoted by the user entering a value lower than -459 (which is the lowest
# possible temperature).

# set heating days to 0
heating_days = 0
# set cooling days to 0
cooling_days = 0

# while temp > -459, keep iterating through and adding into the appropriate variables
while True:
    # asking for the average daily temperature and changing from str to int
    temp = int(input("Enter the average daily temperature: "))
    # if temp <-459, leave the while loop
    if temp < -459:
        break
    # else if temp > 80, add one to cooling_days 
    elif temp > 80:
        cooling_days += 1
    # else if temp < 60, add one too cooling_days
    elif temp < 60:
        heating_days += 1
    
# print the total of heating_days
print(f"Heating days: {heating_days}")
# print the total of cooling_days
print(f"Cooling days: {cooling_days}")