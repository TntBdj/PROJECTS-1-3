from distutils.ccompiler import gen_lib_options
from random import randint, random
import random

#what game to play
while True:
    Game = input("Which game would you like to play? (Enter user guess(ug), computer guess(cg), computer user guess(cug), or type (q) to quit) ")

#user guess game
    if Game == "ug":
        SecretNumber = randint(1, 100)
        Guess = int(input("Try and guess the secret number. It's from 1 to 100: "))
        while Guess != SecretNumber:
            if Guess < SecretNumber:
                print ("The secret number is higher boi!")
            elif Guess > SecretNumber:
                print ("The secret number is less come on man!")
            Guess = int(input("Guess again: "))
        print("You got it. YES SIRRRRRRR!!!!!")

#computer guess game (my version of the game)
    elif Game == "cg":
        SecretNumber = int(input("Make a secret number? (1-100): "))
        x = 1
        y = 100
        Guess = randint(x, y)
        NumberOfGuesses = 1
        while Guess != SecretNumber:
            print(Guess)
            if Guess < SecretNumber:
                x = Guess + 1
            elif Guess > SecretNumber:
                y = Guess - 1
            Guess = randint(x, y)
            NumberOfGuesses = NumberOfGuesses + 1
        print("Your secret number was found. It took the computer " + str(NumberOfGuesses) + " trys to find it. The number was " + str(Guess) + "!")

#user computer guess game (the way they did it on the tutorial)
    elif Game == "cug":
        x = 1
        y = 100
        Guess = randint(x, y)
        while x != y:
            print(Guess)
            UpDown = input("was the guess too big(b), too small(s) or like actually right(r) ")
            if UpDown == "s":
                x = Guess + 1
            elif UpDown == "b":
                y = Guess - 1
            elif UpDown == "r":
                break
            Guess = randint(x, y)
        print("Your secret number was found. The number was " + str(Guess) + "!")

#quit key
    elif Game == "q":
        break

    else:
        print("Invalid input")
        continue

#quit statement 
print ("we done. Come back soon!")
