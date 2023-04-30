freq = {}


def line_words(line):
    word_list = line.split()

    for word in word_list:
        if freq.get(word) is None:
            freq[word] = 1
        else:
            freq[word] = freq.get(word) + 1


with open("lorem_ipsum.txt", "r") as file:
    for line in file:
        line_words(line)

print(freq)
