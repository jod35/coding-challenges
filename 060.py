countries=("Uganda","Kenya","Tanzania","Reanda","Burundi")

for i in countries:
    print(i)

choice=input("Enter a choice: ")

if choice in countries:
    print(f"{choice} is at index {countries.index(choice)}")

else:
    print("The choice is not in the list")


