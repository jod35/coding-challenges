import random

choice=random.randint(1,10)
count=0


while True:
    guess=int(input("Enter your guess between 1 and 10: "))

    if guess <choice:
        print("Your guess is low")
        count+=1

    elif guess > choice:
        print("Your guess is high")
        count+=1

    elif guess== choice:

        count+=1

        print("Well done!\nAttempts: {}".format(count))

        break

    else:
        print("Bad luck\nTry Again")
        count+=1
    
