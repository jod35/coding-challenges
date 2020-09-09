numbers=[123,456,768]

for i in numbers:
    print(i)
    print('\n')

number=int(input("Enter a three digit number: "))

if number in numbers:
    print(f"{number} is in the list")

else:
    print(f"{number} is not in the list")

