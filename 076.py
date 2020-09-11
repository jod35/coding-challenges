
while True:

    password=input("Enter your password: ")

    confirm=input("Confirm your password: ")

    if password != confirm:
        print("Passwords do not match")
        continue


    else:
        print("Success!!!!")
        break

