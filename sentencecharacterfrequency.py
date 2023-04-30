#Input a sequence and count each element's frequency
sentence = "Hello Shlok"

result = {}
for char in sentence:
    if result.get(char.lower()) == None:
        result[char.lower()] = 1
    else:
        result[char.lower()] = result.get(char.lower()) + 1

print(result)
