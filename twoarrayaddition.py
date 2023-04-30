import array

nums1 = array.array("i", [0, 0, 0, 0, 0])
nums2 = array.array("i", [0, 0, 0, 0, 0])

for i in range(5):
    nums1[i] = int(input("Enter 5 integers: "))

for i in range(5):
    nums2[i] = int(input("Enter another 5 integers: "))

result = array.array("i", [0, 0, 0, 0, 0])

for i in range(5):
    result[i] = nums1[i] + nums2[i]

print(result)