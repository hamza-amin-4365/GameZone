import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100.")

# Set the initial number of attempts
attempts = 0

while True:
    # Get the user's guess
    try:
        user_guess = int(input("Guess the number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Increment the number of attempts
    attempts += 1

    # Check if the guess is correct
    if user_guess == secret_number:
        print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
        break
    else:
        # Provide hints for incorrect guesses
        if user_guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

