import random

def choose_difficulty():
    print("\nChoose difficulty:")
    print("1) Easy (1-20, 10 attempts)")
    print("2) Medium (1-50, 7 attempts)")
    print("3) Hard (1-100, 5 attempts)")
    while True:
        choice = input("Enter 1, 2 or 3: ").strip()
        if choice == "1":
            return 1, 20, 10
        if choice == "2":
            return 1, 50, 7
        if choice == "3":
            return 1, 100, 5
        print("Invalid choice — please enter 1, 2 or 3.")

def get_guess(low, high):
    while True:
        val = input(f"Enter your guess ({low}-{high}): ").strip()
        if val.isdigit():
            guess = int(val)
            if low <= guess <= high:
                return guess
            else:
                print(f"Please enter a number between {low} and {high}.")
        else:
            print("That's not a valid number. Try again.")

def play_round():
    low, high, max_attempts = choose_difficulty()
    secret = random.randint(low, high)
    attempts = 0

    print(f"\nI picked a number between {low} and {high}. You have {max_attempts} attempts. Good luck!")

    while attempts < max_attempts:
        guess = get_guess(low, high)
        attempts += 1

        if guess == secret:
            print(f"🎉 Correct! You guessed the number in {attempts} attempt{'s' if attempts>1 else ''}.")
            return True, attempts
        elif guess < secret:
            print("Too low.")
        else:
            print("Too high.")

        remaining = max_attempts - attempts
        if remaining:
            print(f"You have {remaining} attempt{'s' if remaining>1 else ''} left.\n")
        else:
            print("\nNo attempts left.")

    print(f"😢 You lost. The number was {secret}.")
    return False, attempts

def main():
    print("Welcome to Guess the Number!")
    while True:
        play_round()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing — goodbye!")
            break

if __name__ == "__main__":
    main()
