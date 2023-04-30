import array

nums = array.array("i", [0] * 10)

for i in range(10):
    nums[i] = int(input("Enter an integer: "))

left = 0
right = len(nums) - 1

while left < right:
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp
    left = left + 1
    right = right - 1

print(nums)


