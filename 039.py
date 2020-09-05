number =int(input("Please enter a number: "))

count=0

for i in range(1,13):
    print("{} x {} = {}".format(number,count,(count*number)))
    count+=1

