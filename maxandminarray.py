import array
nums = array.array("i", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

for i in range(10):
    nums[i] = int(input("Enter an integer: "))

maximum = 0
minimum = 0

for num in nums:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print(maximum)
print(minimum)
