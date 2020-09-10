count=0

nums=[]

while count< 3:
    num=int(input("Enter a number: "))

    nums.append(num)

    print(nums)

    count +=1

    if count == 3:
        answer=input("Enter 'yes' if you want to remove last item or 'no' to stop")

        if answer == "yes":
            nums.pop()

            print(nums)

        elif answer == "no":
            break
