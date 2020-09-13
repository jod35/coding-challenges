import random
from array import *

count =0
my_arr= array ("i",[])

for i in range(0,5):
    random_=random.randint(10,100)
    my_arr.append(random_)

    count+=1

    if count == 5:
        number=int(input("Enter a number btn 2 and 5: "))

        if number in range(2,6):
            for j in my_arr:
                print("{:.2f}".format(i/number))
                
        else:
            print("Out of range!")

            continue
