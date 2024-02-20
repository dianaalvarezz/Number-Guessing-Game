"""
Number Guessing Game
This script allows the user to play a number guessing game where the user must guess a random number within a specified range and amount of guesses.
Author: Diana Alvarez
Date: 2024-02-20 
"""

import random #generates random numbers
import math #provides logarithm function needed to calculate number of guesses based on range

# Get the Lower and Upper bounds for the guessing range from the player
lowernumber = int(input("Enter the lower bound number: "))
uppernumber = int(input("Enter the upper bound number "))

# Generates the number that is to be guesssed within the specified range
numtoguess = random.randint(lowernumber, uppernumber)

# Informs the player of the amount of chances they have
print("\n\tYou have only ", round(math.log(uppernumber - lowernumber + 1, 2)), " chances to guess the integer!\n")
 
guesses = 0 #Initialize the number of guesses that will be taken

# Loop that will continue until the user runs out of guesses
while guesses < math.log(uppernumber - lowernumber + 1, 2):
    guesses += 1 # Increments the amount of guesses
    guess = int(input("Guess a number:- ")) # Promts player the guess 

    # Checks to see if the guess was correct, too high, or too low
    if numtoguess == guess:
        print("Congratulations you did it in ", guesses, " tries")
        break
    elif numtoguess > guess:
        print("The number you guesses is too small!")
    elif numtoguess < guess:
        print("The number you guesses is too large!")

# If player runs out of chances than allowed the game will give themm the correct answer
if guesses > math.log(uppernumber - lowernumber + 1, 2):
        print("\nThe number was ", numtoguess, ". Nice try!")
        
          
