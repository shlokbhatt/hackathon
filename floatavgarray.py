import array
floats = array.array("f", [0, 0, 0, 0, 0])

for i in range(5):
    floats[i] = float(input("Enter a float: "))

total = 0

for num in floats:
    total = total + num

mean = total / len(floats)

print(mean)

