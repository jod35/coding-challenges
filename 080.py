from array import *

my_nums=array ('i',[])

for i in range(0,5):
    number=int(input("Enter a number: "))

    if number in range(10,20):
        my_nums.append(number)
    else:
        print("Out of range")
        continue
print("Thank you")

for i in my_nums:
    print(i)



        
