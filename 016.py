answer=input("Is it raining ?")

if answer== "yes":
    second=input("Is it windy?")
    if second == "yes":
        print("It is too windy for an umbrella")
elif answer == "no":
    print("Take an umbrella")
else:
    print("Have a nice day")

