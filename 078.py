from array import *

#incomplete
my_integers=array ('i',[])

count=0

while count <5:
    num=int(input("Enter a number: "))

    
    my_integers.append(num)

    count+=1

    if count==5:
        print(type(my_integers))
        
        reversed_=my_integers.reverse()

        print(my_integers)
        break

