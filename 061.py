countries=("Uganda","Kenya","Tanzania","Rwanda")

try:
    choice =int(input("Enter an index: "))

    print(f"{countries[choice]} is in the index {choice}")
except IndexError:
    print("The index is out of range")





