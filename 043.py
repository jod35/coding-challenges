print("Please choose the direction of counting\n1.Upward\n2.Downward")

option=int(input(">>>> "))
count=0

if option ==1:
    max_number=int(input("Enter max value: "))
    min_number=int(input("Enter min value: "))

    for i in range(min_number,(max_number)):
        print(i)
        count+=1

elif option ==2:
    max_value=int(input("Enter the max value: "))
    

    for i in range(0,max_value):
        print(max_value)
        max_value -=1


