
word=input("Enter a word: ")
#this is pig latin
#take the first consonant of the word
#take it to the end of the word and add "ay"


consonants=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

if word[0] in consonants:
    final=word[1:len(word)] + word[0]+"ay"
    print(final)
