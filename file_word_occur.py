# Write a Python program that reads in a text file
# and prints out the number of occurrences of each word in the file.
word_counts = {}
with open("lorem_ipsum.txt", 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
    for word, count in word_counts.items():
        print(f'{word}: {count}')