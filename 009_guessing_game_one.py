import random

def main():
    num = random.randint(0, 100)
    guesses = 0
    total_guesses = 0
    games_played = 0

    print("Number Guessing Game\n")
    print("Enter 'exit' to quit\n\n")

    while True:
        try:
            guess = input("Guess the number (0-100): ")

            if guess.lower() == "exit":
                if games_played > 0:
                    guess_average = total_guesses / games_played
                    print(f"\nGame Exited. Your average number of guesses for completed games was {guess_average:.2f}")
                else:
                    print("Game Exited. No completed games to calculate average.")
                break
            
            guess = int(guess)

            if guess < 0 or guess > 100:
                print("Enter a number from 0 to 100")
                continue

            guesses += 1

            if guess > num:
                print("Too high")
            elif guess < num:
                print("Too low")
            else:           
                print(f"You guessed the correct number in {guesses} tries")
                games_played += 1        
                total_guesses += guesses 
                
                play_again = input("Do you want to play again? (Y/N): ") 

                if play_again.lower() in ["y", "yes"]:
                    num = random.randint(0, 100)
                    guesses = 0         
                else:
                    guess_average = total_guesses / games_played
                    print(f"Your average number of guesses is {guess_average:.2f}")
                    break
                    
        except ValueError:
            print("Enter a valid number")

if __name__ == "__main__":
    main()