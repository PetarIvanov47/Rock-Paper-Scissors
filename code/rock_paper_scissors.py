import random

print("Enter your name:", end="")
player_one = input()
print(f"Hello {player_one}!")
player_two = "Computer"
choices = ["rock", "paper", "scissors"]

flag = False
print("Do you wanna play?")
answer = input()
if answer == "no":
    print("Ok, bye!")
    exit()

print("OK, let's play")

while True:
    player_one_choice = input()
    computer_choice = random.choice(choices)

    if player_one_choice == "rock" and computer_choice == "paper":
        print(f"{computer_choice}")
        break

    elif player_one_choice == "rock" and computer_choice == "scissors":
        print(f"{computer_choice}")
        flag = True
        break

    elif player_one_choice == "rock" and computer_choice == "rock":
        print(f"{computer_choice}")
        print("Draw")
        continue

    elif player_one_choice == "paper" and computer_choice == "rock":
        print(f"{computer_choice}")
        flag = True
        break

    elif player_one_choice == "paper" and computer_choice == "paper":
        print(f"{computer_choice}")
        print("Draw")
        continue

    elif player_one_choice == "paper" and computer_choice == "scissors":
        print(f"{computer_choice}")
        break

    elif player_one_choice == "scissors" and computer_choice == "rock":
        print(f"{computer_choice}")
        break

    elif player_one_choice == "scissors" and computer_choice == "paper":
        print(f"{computer_choice}")
        flag = True
        break

    elif player_one_choice == "scissors" and computer_choice == "scissors":
        print(f"{computer_choice}")
        print("Draw")
        continue

if flag:
    print(f"{player_one} Wins!")
else:
    print(f"The computer Wins!")
