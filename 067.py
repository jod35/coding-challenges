people=[]

answer=""

while answer != "no":
    person=input("Enter a person you would like to invite to a party: ")

    print("\n")

    answer=input("Enter 'yes' to continue adding or 'no' to stop adding people: ")
    
    print("\n")
    

    people.append(person)

    if answer == "yes":
        
        print("People invited: {}".format(len(people)))

        continue

    elif answer == "no":
        print("Stopped!\nPeople invited: {} \n".format(len(people)))

    else:
        print("Unknown option")



