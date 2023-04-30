num = int(input("Enter an integer: "))
binary = bin(num)
count = binary[2:].count('1')
print(count)