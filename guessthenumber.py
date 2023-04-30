#Guess the Number: Write a program that generates a random number between
# 1 and 100, and asks the user to guess what the number is. If the user's
# guess is too high or too low, the program should give a hint and ask the
# user to guess again. The program should keep track of the number of
# guesses it takes the user to correctly guess the number.
import random
random_num = random.randint(1, 100)
print(random_num)

num_guesses = 0
while True:
    num_guesses = num_guesses + 1
    guess = int(input("Guess the number: "))
    if guess > random_num:
        print("Too high! Try again: ")
    elif guess < random_num:
        print("Too low! Try again: ")
    else:
        print("Correct!")
        break

print(num_guesses)


