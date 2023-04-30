import array

nums1 = array.array("i", [0, 0, 0, 0, 0])
nums2 = array.array("i", [0, 0, 0, 0, 0])
result = array.array("i", [0, 0, 0, 0, 0])

for i in range(5):
    nums1[i] = int(input("Enter first set of five integers: "))
    nums2[i] = int(input("Enter second set of five integers: "))
    result[i] = nums1[i] + nums2[i]

print(result)