total=0

while total <= 50:
    number=int(input("Enter a number: "))
    total+=number

    if total >= 50:
        print("Enough! The total is {}".format(total))
        

