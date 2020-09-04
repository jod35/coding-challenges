print("1)square\n2)triangle\n\nEnter an option")

option=int(input(">>> "))

if option == 1:
    side=int(input("Enter length of side: "))
    area=side*side
    print("The area of a square with a side of {} units is {}".format(side,area))
elif option ==2:
    base=int(input("Enter the base: "))
    height=int(input("Enter the height: "))
    area=0.5 * height * base
    print("The area of a triangle with a base {} and height {} is {}".format(base,height,area))

