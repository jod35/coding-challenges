print("1) Create a file\n2) Display a file\n3) Add a new item to the file\nEnter options 1,2,3")

option=int(input(">>>> "))


if option == 1:
    file_=open("Subjects.txt","w")
    subject=input("Enter a subject: ")

    file_.write(subject)
    file_.close()
elif option == 2:
    file_=open("Subjects.txt","r")
    print(file_.read())
elif option == 3:
    file_=open("Subjects.txt","a")
    subject=input("Enter a subject: ")

    file_.write(subject)
    file_.close()
else:
    print("Please enter 1,2 or 3")

