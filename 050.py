count=0
while True:
    number=int(input("Enter a number between 10 and 20: "))

    if number <10:
        print("Too low")
        count+=1

    elif number>20:
        print("Too high")
        count+=1

    else:
        count+=1
        print("Well done!!\nAttempts: {}".format(count))
        break
