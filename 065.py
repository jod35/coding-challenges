
colours=["red","green","blue","indigo","purple","maroon","violet","crimson","yellow","cyan","coral"]


first_index=int(input("Enter the first index (0-4) "))

second_index=int(input("Enter the second index (5-9) "))

result=colours[first_index:second_index]

print(f"colours[{first_index}:{second_index}] is {result}")
