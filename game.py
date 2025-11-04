import random

chances = 0
level = 0
number = 0
total_attemps = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 chances to guess the correct number.")

print("Please select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

level = int(input("Enter your choice: "))

if level == 1: 
    print("Great! You have selected the Easy difficulty level")
    chances = 10
elif level == 2: 
    print("Great! You have selected the Medium difficulty level")
    chances = 5
elif level == 3: 
    print("Great! You have selected the Hard difficulty level")
    chances = 3
total_attemps = chances
print("Let's start the game!")

number_to_guess = random.randint(1, 100)

while chances > 0:
    number = int(input("Enter your guess: "))
    if(number > number_to_guess):
        print("Incorrect! The number is less than ", number)
        chances -= 1
    elif(number < number_to_guess):
        print ("Incorrect! The number is greater than ", number)
        chances -= 1
    else:
        print(f"Congrulations! You guessed the number in {total_attemps - chances} attemps.")
        break
