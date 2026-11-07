import random


def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("===== NUMBER GUESSING GAME =====")
    print("Guess a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if not 1 <= guess <= 100:
            print("Choose a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break


if __name__ == "__main__":
    play_game()