import random   # to let computer choose randomly

def play_game():
    choices = ["stone", "paper", "scissors"]   # possible moves
    print("Choices:", choices)

    # Step 1: player chooses
    player = input("Enter your choice (stone/paper/scissors): ").lower()
    print("You chose:", player)

    # Step 2: computer chooses
    computer = random.choice(choices)
    print("Computer chose:", computer)

    # Step 3: decide winner
    if player == computer:
        print("Result: It's a draw!")
    elif (player == "stone" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "stone"):
        print("Result: You win!")
    else:
        print("Result: Computer wins!")

# Run the game
play_game()
