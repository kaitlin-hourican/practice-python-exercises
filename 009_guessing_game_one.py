import random

def main():
    num = random.randint(1, 9)
    guess_count = 0

    print("Number Guessing Game\n")
    print("Enter 'exit' to quit\n\n")

    while True:
        try:
            guess = input("Guess the number (1-9): ")

            if guess == "exit":
                print("Game Exited")
                break
            else:
                guess = int(guess)

            if guess < 1 or guess > 9:
                print("Enter a number from 1 to 9")
                continue

            guess_count += 1
            
            if guess == num:
                print(f"You guessed the correct number in {guess_count} tries")
                break
        except ValueError:
            print("Enter a valid number")

if __name__ == "__main__":
    main()
