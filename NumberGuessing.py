# Number Guessing 

import random

def main():
    randomNum = randomNumber()
    askUserForNumber(randomNum)

def randomNumber():
    numbers = list(range(1,101))
    randomNumber = random.choice(numbers)
    print(randomNumber)
    return randomNumber

def askUserForNumber(randomNum):
    guessedNumber = 0
    hints = []
    while guessedNumber != randomNum:
        guessedNumber = int(input("Guess a number: "))
        print("That was not the correct number. Try again")
        returnedHint = higherOrLower(randomNum, guessedNumber)
        hints.append(returnedHint)
        for hint in hints:
            print(hint)
        
    print(f"You guessed right! The number was: {randomNum}")

def higherOrLower(randomNum, guessedNumber):
    if guessedNumber > randomNum:
        hint =(f"{guessedNumber} is to high")
        return hint
    else:
        hint = (f"{guessedNumber} is to low")
        return hint
main()