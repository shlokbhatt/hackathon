#Write a program that takes a list of numbers as input and returns the sum of even numbers in it.

list = []
num = -1
while num != 0:
    num = int(input("What is your number? "))
    if num != 0:
        list.append(num)

print(list)

sum_even = 0

for num in list:
    if num % 2 == 0:
        sum_even = sum_even + num

print(sum_even)