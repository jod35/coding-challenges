compnum=50

count=0


while True:
    guess =int(input("Enter yout guess: "))
    if guess < compnum:
        print("Too low, Try again")
        count+=1
    elif guess >compnum:
        print("Too high,Try again")
        count+=1
    elif guess == compnum:
        count+=1
        print("Well done, you took {} guesses.".format(count))
        break
