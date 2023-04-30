import array
nums = array.array("i", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

for i in range(10):
    nums[i] = int(input("Enter an integer: "))

for num in nums:
    if num % 2 == 0:
        nums.remove(num)

print(nums)