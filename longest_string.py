# Write a program that takes a list of strings as input and returns the longest string in it.
list = []
string = ""
while string != "Quit":
    string = input("Enter a string: ")
    list.append(string)
list.remove("Quit")
result = ""
for item in list:
    if len(item) > len(result):
        result = item

print(result)
