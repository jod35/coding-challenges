from array import *
import random

my_nums=array ("i",[])
count=0

while count <5:
    random_=random.randint(0,50)



    my_nums.append(random_)
    count+=1

    if count ==5:
        print(my_nums)
        break



