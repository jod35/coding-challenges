firstname=input("Enter your firet name: ")

if len(firstname) > 5:
    print(str.lower(firstname))
else:
    surname=input("Your firstname is short, please enter your surname: ")
    print(str.upper(firstname+surname))
