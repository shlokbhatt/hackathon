nums = [2, 5, 9, 2, 8, 5, 10, 2, 2, 10]
freq = {}
for num in nums:

    if freq.get(num) is None:
        freq[num] = 1
    else:
        freq[num] = freq.get(num) + 1

print(freq)
