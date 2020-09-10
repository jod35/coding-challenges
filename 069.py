tv_programmes=["Rick and Monty","Silicon Valley","Game of thrones","Mr Robot"]

count=0
answer=""

while answer != "no":

    answer=input("Enter 'yes' to comtinue or 'no' to stop")
    if answer  == "yes":

        print("/n The TV programmmes are:")
        for i in tv_programmes:
            print(f"{count}) {i}")
            count+=1

        programme=input("Enter a TV show: ")
        index=int(input("Enter an index you want: "))


        tv_programmes.insert(index,programme)
        
    elif answer == "no":
        for i in tv_programmes:
            print(f"{count}) {i}")
            break

