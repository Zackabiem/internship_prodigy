import random
import time

# Global variable to track high score
high_score = None

def choose_difficulty():
    """Allow the user to choose a difficulty level."""
    print("\nChoose a difficulty level:")
    print("1. Easy (1 to 50)")
    print("2. Medium (1 to 100)")
    print("3. Hard (1 to 200)")
    
    while True:
        try:
            choice = input("Enter your choice (1, 2, or 3, or type 'stop' to quit): ").lower()
            if choice == "stop":
                print("Game stopped. Goodbye!")
                return None
            choice = int(choice)
            if choice == 1:
                return 50
            elif choice == 2:
                return 100
            elif choice == 3:
                return 200
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number or type 'stop'.")

def provide_hint(number):
    """Provide hints to the user."""
    hints = []
    if number % 2 == 0:
        hints.append("Hint: The number is even.")
    else:
        hints.append("Hint: The number is odd.")
    if number % 3 == 0:
        hints.append("Hint: The number is divisible by 3.")
    print(random.choice(hints))

def update_high_score(attempts):
    """Update and display the high score."""
    global high_score
    if high_score is None or attempts < high_score:
        high_score = attempts
        print(f"🎉 New high score: {attempts} attempts!")

def play_again():
    """Ask the user if they want to play again."""
    while True:
        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay in ["yes", "y"]:
            return True
        elif replay in ["no", "n"]:
            return False
        else:
            print("Please answer with yes or no.")

def guessing_game():
    """Main function to run the guessing game."""
    print("Welcome to the Guessing Game!")
    while True:
        # Difficulty selection
        max_range = choose_difficulty()
        if max_range is None:
            break  # Stop the game if the user chooses "stop"

        number_to_guess = random.randint(1, max_range)
        max_attempts = 10
        attempts = 0

        print(f"\nGuess the number between 1 and {max_range}. You have {max_attempts} attempts!")
        print("Type 'stop' at any time to quit the game.")
        start_time = time.time()

        while attempts < max_attempts:
            try:
                user_input = input("\nEnter your guess: ").lower()
                if user_input == "stop":
                    print("Game stopped. Goodbye!")
                    return
                user_guess = int(user_input)
                attempts += 1

                if user_guess < number_to_guess:
                    print("Too low!")
                    provide_hint(number_to_guess)
                elif user_guess > number_to_guess:
                    print("Too high!")
                    provide_hint(number_to_guess)
                else:
                    print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
                    end_time = time.time()
                    print(f"Time taken: {end_time - start_time:.2f} seconds.")
                    update_high_score(attempts)
                    break
            except ValueError:
                print("Invalid input. Please enter a number or type 'stop' to quit.")

        if attempts == max_attempts and user_guess != number_to_guess:
            print(f"\nGame over! The number was {number_to_guess}.")

        # Play again prompt
        if not play_again():
            print("Thanks for playing! Goodbye!")
            break

# Run the game
guessing_game()
