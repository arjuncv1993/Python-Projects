# Rock Paper Scissor Game

import random

player_wins = 0
computer_wins = 0

while True:
    choices = ["rock", "paper", "scissors"]
    player = input("Enter your choise :: ").lower()
    computer = random.choice(choices)
    if player in choices:
        if player == computer:
            print("Player :: ", player)
            print("Computer :: ", computer)
            print("Tie")
        elif player == "rock":
            if computer == "paper":
                print("Player :: ", player)
                print("Computer :: ", computer)
                print("Computer Wins")
                computer_wins += 1
            elif computer == "scissors":
                print("Player :: ", player)
                print("Computer :: ", computer)
                print("Player Wins")
                player_wins += 1
        elif player == "paper":
            if computer == "rock":
                print("Player :: ", player)
                print("Computer :: ", computer)
                print("Player Wins")
                player_wins += 1
            elif computer == "scissors":
                print("Player :: ", player)
                print("Computer :: ", computer)
                print("Computer Wins")
                computer_wins += 1
        elif player == "scissors":
            if computer == "rock":
                print("Player :: ", player)
                print("Computer :: ", computer)
                print("Computer Wins")
                computer_wins += 1
            elif computer == "paper":
                print("Player :: ", player)
                print("Computer :: ", computer)
                print("Computer Wins")
                computer_wins += 1
    else:
        print("Please enter a valid choice.!")
        
    play_again = input("Play again? Yes/No   ").lower()
        
    if play_again != "yes":
        break
    else:
        continue

print(f"Player have won {player_wins} times")
print(f"Computer have won {computer_wins} times")
print("Bye!!")

