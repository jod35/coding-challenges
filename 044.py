number=int(input("Enter the number of people you want to invite for the party: "))

people=[]

if number <10:
    for i in range(0,number):
        person=input("Enter name of person: ")
        people.append(person)
    for j in people:
        print(f"{j} has been invited to the party")
else:
    print("Too many people, Not invited")


