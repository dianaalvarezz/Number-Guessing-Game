import random
import math

lowernumber = int(input("Enter the lower bound number: "))
uppernumber = int(input("Enter the upper bound number "))

x = random.randint(lowernumber, uppernumber)
print("\n\tYou have only ",
    round(math.log(uppernumber - lowernumber + 1, 2)),
    " chances to guess the integer!\n")
 
guesses = 0

while guesses < math.log(uppernumber - lowernumber + 1, 2):
    guesses += 1

    guess = int(input("Guess a number:- "))

    if x == guess:
        print("Congratulations you did it in ",
              guesses, " tries")
        
        m

