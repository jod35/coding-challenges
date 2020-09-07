import random
while True:
    choice=input("Enter 'h' or 't': ")

    right_choice=random.choice(["h","t"])

    if choice == right_choice:
        print("Congs!!!!\nMy guess is {}".format(right_choice))
        break
    else:
        print("No please, Try again!")

