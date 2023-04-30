#Write a program that takes a sentence as input and prints the number of vowels in it.
sentence = input("Enter your sentence: ")
vowels = "aeiou"
count = 0
for char in sentence:
    if char.lower() in vowels:
        count = count + 1

print(count)
