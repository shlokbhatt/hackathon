pal = input("Enter a word: ")
isPal = True
left = 0
right = len(pal) - 1

while left < right:
    if pal[left] != pal[right]:
        isPal = False
        break
    left = left + 1
    right = right - 1

print(isPal)
