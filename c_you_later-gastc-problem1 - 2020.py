# Input: Prompt the user to type in their desired phrase, and read it in.
# Output: You should print out the phrase without every occurrence of ‘c’

sentence = input("Enter a sentence: ")
sentence = sentence.lower()
print(sentence.replace("c", ""))

