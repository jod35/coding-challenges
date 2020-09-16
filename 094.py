file_n=open("Numbers.txt","w")

for i in range(0,5):
    number=int(input("Enter a number: "))
    file_n.write(f"{number},")

file_n.close()


