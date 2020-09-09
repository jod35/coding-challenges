subjects=["Mathematics","Physics","History","Chemistry","Geography","Biology"]


for i in subjects:
    print(i)

print('\n')

subject=input("Please enter a subject you dont like from the subjects: ")

if subject in subjects:
    subjects.remove(subject)

print(subjects)


