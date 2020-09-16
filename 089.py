shoe_data={}
shoes=[]
count=0

while count< 5:
    name=input("Enter a name: ")
    age=int(input("Enter an age: "))
    shoe_size=int(input("Enter a shoe size: "))

    shoe_data["name"]=name
    shoe_data["age"]=age
    shoe_data["shoe_size"]=shoe_size

    shoes.append(shoe_data)


    count +=1

    if count == 5:
        print(shoes)
        break
