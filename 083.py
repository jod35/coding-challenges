from array import *

my_arr= array("i",[])


count=0


while count <5:
    number=int(input("Enter a number: "))

    my_arr.append(number)

    count+=1


    if count == 5:
        print("\n {}".format(my_arr))

        number_to_check=int(input("Enter a number: "))


        if number in my_arr:
            pos=my_arr.index(number_to_check)
            print("{} is in position {}".format(number_to_check,pos))

        else:
            print("{} is not in the list".format(number_to_check))


        break



