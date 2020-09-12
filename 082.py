from array import *

first_arr=array ("i",[1,2,3])

second_arr=array ("i",[4,5,6])

first_arr.extend(second_arr)

sorted(first_arr)

for i in first_arr:
    print(i)
