#Your job is to write a program that will take one sentence
# as input and output whether or not the sentence is considered
# “pi friendly”. Note that it does not matter if a letter is uppercase or lowercase.

sentence = input("Enter a sentence: ")
sentence = sentence.lower()
count = sentence.count("pi")

if count == 3 or count == 1 or count == 4:
    print("pi friendly")
else:
    print("not pi friendly")

