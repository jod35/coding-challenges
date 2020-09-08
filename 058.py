import random

count=0
score=0

while count<5:
    first_num=random.randint(1,100)
    second_num=random.randint(1,100)

    sum_=first_num + second_num
    count+=1

    print(f"{count})What is the output of {first_num} + {second_num}")

    answer=int(input(">>> "))

    if answer == sum_:
        score+=1
        print("Correct!!\nScore: {}/5\n".format(score))

        

    else:
        print("Wrong answer\nScore: {}/5\n".format(score))
        


