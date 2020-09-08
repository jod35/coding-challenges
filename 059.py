import random

chance=random.choice(["GREEN","RED","BLUE","YELLOW"])

count=0

while True:
    print("Choose a colour:\n1.GREEN\n2.RED\n3.BLUE\n4.YELLOW\n")
    choice=input(">>> ")
    count+=1

    if choice ==chance:
        print("Well done, you chose the right colour\nAttempt: {}\n".format(count))
        break
    else:
        if chance=="YELLOW":
            print("Yellow Mellow")

        elif chance == "RED":
            print("Blood is red, I love yiu")
        elif chance == "BLUE":
            print("Wait, is water blue?")

        elif chance == "GREEN":
            print("Why are you so green aabout things?")

