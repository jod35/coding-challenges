number=int(input("Enter a number less than 50: "))

count=50

for i in range (0,number-1):
    print(count)
    count-=1
    if count == number:
        break
