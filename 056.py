import random

choice=random.randint(1,10)
count=0

while True:
    guess =int(input("Enter your guess: "))
    if guess ==choice:
        count+=1

        print("Well done!!!\n Attempts: {} ".format(count))

        break

    else:
        print("Wrong choice!\nPlease try again")
        count+=1




