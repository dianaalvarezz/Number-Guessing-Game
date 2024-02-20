import random
import math

lowernumber = int(input("Enter the lower bound number: "))
uppernumber = int(input("Enter the upper bound number "))

numtoguess = random.randint(lowernumber, uppernumber)
print("\n\tYou have only ",
    round(math.log(uppernumber - lowernumber + 1, 2)),
    " chances to guess the integer!\n")
 
guesses = 0

while guesses < math.log(uppernumber - lowernumber + 1, 2):
    guesses += 1

    guess = int(input("Guess a number:- "))

    if numtoguess == guess:
        print("Congratulations you did it in ",
              guesses, " tries")
        
        break
    elif numtoguess > guess:
        print("The number you guesses is too small!")
    elif numtoguess < guess:
        print("The number you guesses is too large!")

if guesses > math.log(uppernumber - lowernumber + 1, 2):
        print("\nThe number was ", numtoguess, ". Nice try!")
        
          
