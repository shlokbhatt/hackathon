sentence = input("Enter your sentence: ")
def words_starting_with_vowel(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = sentence.split()
    vowel_words = []
    for word in words:
        if word[0].lower() in vowels:
            vowel_words.append(word)
    return vowel_words

print(words_starting_with_vowel(sentence))