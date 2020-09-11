uppercase_word=""

while not uppercase_word.isupper():
    uppercase_word=input("Enter a word in uppercase: ")

    if uppercase_word.isupper():
        print("Correct")
        break

    else:
        print("Enter in lowercase")
        continue
