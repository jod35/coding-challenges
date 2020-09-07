import random

count=0
score=0

while count<5:
    first_num=random.randint(1,100)
    second_num=random.randint(1,100)

    sum_=first_num + second_num

    print(f"What is the output of {first_num} + {second_num}")

    answer=int(input(">>> "))

    if answer == sum_:
        score+=1
        print("Correct!!\nScore: {}/5".format(score))

        count+=1

    else:
        print("Wrong answer\nScore: {}/5".format(score))
        count+=1


