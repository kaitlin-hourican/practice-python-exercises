import random

def main():
    print("Welcome to Rock Paper Scissors!")
    while True:
        continue_playing = input("Enter 'Y' to play. ").upper()

        if continue_playing == "Y":
            play_game()
            print("Thanks for playing")
        else:
            break


def play_game():
    valid_moves = ["rock", "paper", "scissors"]
    print("To play: enter 'rock', 'paper', or 'scissors'")

    while True:
        player_move = input("What's your move? ").lower()

        if player_move in valid_moves:
            break
        print("Enter valid move")

    computer_move = random.choice(valid_moves)

    print(f"Player: {player_move} ... vs ... {computer_move} : Computer")
    print(get_winner(player_move, computer_move))
            
def get_winner(player, computer):
    if player == computer:
        return "Tie"

    if player == "rock":
        return "Player wins" if computer == "scissors" else "Computer wins"
    elif player == "paper":
         return "Player wins" if computer == "rock" else "Computer wins"
    else:
         return "Player wins" if computer == "paper" else "Computer wins"


if __name__ == "__main__":
    main()