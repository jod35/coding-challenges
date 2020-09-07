count=0
people=[]

while True:
    person=input("Enter the name of a person: ")
    
    people.append(person)

    option=int(input("Enter 1 to add another or anything else to stop: "))

    if option == 1:
        continue
    else:
        print(f"{len(people)} people have been invited to the party")
        break

