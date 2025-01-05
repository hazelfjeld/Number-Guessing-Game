import random
import time

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")

    # Difficulty levels
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    # Select difficulty
    while True:
        try:
            choice = int(input("\nEnter your choice (1/2/3): "))
            if choice == 1:
                chances = 10
                break
            elif choice == 2:
                chances = 5
                break
            elif choice == 3:
                chances = 3
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print(f"\nGreat! You have selected {chances} chances.")
    print("Let's start the game!\n")

    # Generate random number
    number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()  # Timer starts

    # Game loop
    while chances > 0:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == number:
                end_time = time.time()  # Timer ends
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                print(f"Time taken: {round(end_time - start_time, 2)} seconds.")
                break
            elif guess < number:
                print("Incorrect! The number is greater than", guess)
            else:
                print("Incorrect! The number is less than", guess)

            chances -= 1
            if chances == 0:
                print(f"\nGame Over! The correct number was {number}.")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Main loop
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Goodbye!")
        break



