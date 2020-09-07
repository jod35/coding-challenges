import random

choice=random.randint(0,5)
guesses =0
while True:
    guess=int(input("Enter your guess: "))

    if guess !=choice:
        print("Bad luck")
        guesses+=1

    else:
        guesses+=1
        print("Well done\nAttempts: {}".format(guesses))
        
        break
