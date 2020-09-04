import math

radius=float(input("Enter a radius: "))
depth=float(input("Enter a depth: "))

circle_area=math.pi * (radius*radius)

volume=circle_area *depth

print("The volume of a cylinder with radius {} and depth {} is {:.2f}".format(radius,depth,volume))

