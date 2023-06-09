import random

print("Hello and welcome!") 
print("lets initiate the game conditions")

while True:
    x = input("Type a number, such that the guessing game takes place between 1 and the typed number: ")
    #Checking if the typed digit is number or not
    if x.isdigit():
        print("")
        x = int(x)
        break
    else:
        print("ERROR, Type a positive number please: ")

random_number = random.randint(1, x)

while True:
    Difficulty = input("Type easy (if hints are needed) or hard (if no hints are needed): ")
    Difficulty = Difficulty.lower()

    if Difficulty != "easy" and Difficulty != "hard":
        print("Please type the word (easy or hard) with correct spellings")
    else:
        print("")
        print("Lets finally start the game")
        break

if Difficulty=="easy":
    guess = 0
    count = 1   #Starts with 1 because, its covering the case when the guessed number is equal to random number.
    while guess != random_number:
        guess = input(f"Guess the secret number between 1 and {x}: ")

        if guess.isdigit():  #Checking if the guess is a number.
            guess = int(guess)
        else:
            print("Error, Type a number")
            continue

        if guess < random_number:
            print("Please Guess again, Too low.")
            count += 1
        elif guess > random_number:
            print("Please Guess again, Too high.")
            count += 1
    print(f"Congratulations you guessed the random number {random_number} in {count} number of guesses.")

else:
    guess=0
    count =1
    while guess!= random_number:
        guess= input(f"Guess the secret number between 1 and {x}: ")
        
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Error, Type a number")
            continue

        if guess != random_number:
            print("Please Guess again.")    
            count +=1
    print(f"Congratulations you guessed the random number {random_number} in {count} number of guesses.")