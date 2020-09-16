file_=open("Names","w")

for i in range(0,5):
    name=input("Enter a name: ")

    file_.write(f"{name} \n")

file_.close()
