#Write a program that takes a string as input and prints the reverse of it.
#string = input("Enter a string: ")
name = input("Enter a name: ")
count = len(name) - 1
while count >= 0:
    print(name[count], end = "")
    count = count - 1
