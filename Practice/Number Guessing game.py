import random
number = random.randint(1,100)
guess_limit=5
guess_guesses = 0
while guess_guesses < guess_limit:
    guess = int(input("Guess a number between 1 and 100: "))
    guess_guesses += 1
    if guess<number:
        print("Too low")
        print(f"{5-guess_guesses} guesses left")
    elif guess> 100:
        print("Error!!! Enter a number between 1 and 100")
        break
    elif guess>number:
        print("Too high")
        print(f"{5-guess_guesses} guesses left")
    else :
        print("Correct")
        break
print(f"The correct number was {number}")
