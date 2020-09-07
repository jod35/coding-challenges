#ten bottles hanging on the wall

num =10

while True:
    print("There are {} bottles hanging on the wall, if 1 falls, how many bottles remain haging on the wall?".format(num))

    answer=int(input(">>>> "))

    if (answer == (num-1)) and (answer > 0):
        num-=1
        continue

    elif (num ==1) and (answer== 0):
        print("There are no more bottles in hanging on the wall")
        break

    else:
        print("Try again")


