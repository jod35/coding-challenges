total =0
while True:
    number=int(input("Enter a number: "))
    total+=number
    option=input("Enter  'y' to vintinue adding or any thing else yo stop: ")
    if option == "y":
        continue
    else:
        print("The total is {}".format(total))
        break


