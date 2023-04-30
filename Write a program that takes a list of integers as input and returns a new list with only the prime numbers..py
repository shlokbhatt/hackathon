num = int(input("Enter a number: "))
num_prime = 0
if num > 1:
    for i in range(2, int(num / 2) + 1):
        if (num % i) > 0:
            num_prime = num_prime + 1
print(num_prime)



