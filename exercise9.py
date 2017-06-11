import random

numOfGuesses = 0
guesses = []
randNum = random.randint(1, 9)
isGuessed = False

def checkIfDuplicate(userGuess):
    for guess in guesses:
        if guess == userGuess:
            print("Hey nerd, you already guessed " + str(userGuess))

def checkIfGuessed(guess):
    if guess == randNum:
        print("Great job picking " + str(guess) + "!")
        return True
    elif guess > randNum:
        print("Too high!")
    elif guess < randNum:
        print("Too Low")
    else:
        print("Error")

while not isGuessed:
    userGuess = int(input("Enter a number to guess: "))
    guesses.append(userGuess)
    checkIfDuplicate(userGuess)
    numOfGuesses += 1
    isGuessed = checkIfGuessed(userGuess)


print("You won!!!\nNumber of Guesses: " + str(numOfGuesses))
