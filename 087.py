my_list=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

row=int(input("Enter the row: "))
print(my_list[row])

col=int(input("Enter the col: "))

print(my_list[row][col])

option=input(("Enter 'yes' to print a number in the column or 'no' to stop: "))

if option == "yes":
    number=int(input("Enter a number: "))

    print(number)

    if number:
        my_list[row][col]=number
        print(f"The new column is {my_list[row]}")
    


