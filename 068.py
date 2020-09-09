people=[]

answer=""
count=1

while answer != "no":
    answer=input("\nEnter 'yes' to continue or 'no'\n")

    if answer == "yes":
        person=input("\nEnter a name of a person you want to invite: ")

        people.append(person)
        

    elif answer == "no":
        if len(people) > 0:
            for i in people:
                print(f"{count}) {i}")

                count+=1

            print(f"The number of people is {len(people)}")

    else:
        print("Unknown option, Please use 'yes' or 'no'")


                


            

    
