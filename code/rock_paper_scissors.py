import random

# menu
player_one = input("Enter your name:").title()
print(f"Hello {player_one}!")
player_two = "Computer"
choices = ["rock", "paper", "scissors"]
print("Do you wanna play?")
answer = input()

while True:
    if answer == "no":
        print("Ok, bye!")
        exit()
    elif answer == "yes":
        print("OK, let's play.")
        break

    else:
        print("Incorrect answer!")
        print("You have to answer with 'yes' or 'no'.")
        answer = input()

print("Please select game mode.")
game_mode = input("Enter '1' for first to win or enter '2' for first to two wins from three games.")

# first to win
if game_mode == "1":
    print("First to win.")
    print("Start!")
    flag = False
    while True:
        player_one_choice = input("Choose between [rock, paper, scissors]: ")
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
        print(f"The {player_two} Wins!")

# 2 from 3
elif game_mode == "2":
    print("2 from 3")
    print("Start!")
    counter_player_one = 0
    counter_player_two = 0
    while counter_player_one < 2 and counter_player_two < 2:
        player_one_choice = input("Choose between [rock, paper, scissors]: ")
        computer_choice = random.choice(choices)

        if player_one_choice == "rock" and computer_choice == "paper":
            print(f"{computer_choice}")
            print(f"Point for the {player_two}!")
            counter_player_two += 1
            print(f"Result: {player_one}-{counter_player_one} : {player_two}-{counter_player_two}")

        elif player_one_choice == "rock" and computer_choice == "scissors":
            print(f"{computer_choice}")
            print(f"Point for {player_one}!")
            counter_player_one += 1
            print(f"Result: {player_one}-{counter_player_one} : {player_two}-{counter_player_two}")

        elif player_one_choice == "rock" and computer_choice == "rock":
            print(f"{computer_choice}")
            print("Draw!")
            print(f"Result: {player_one}-{counter_player_one} : {player_two}-{counter_player_two}")

        elif player_one_choice == "paper" and computer_choice == "rock":
            print(f"{computer_choice}")
            print(f"Point for {player_one}!")
            counter_player_one += 1
            print(f"Result: {player_one}-{counter_player_one} : {player_two}-{counter_player_two}")

        elif player_one_choice == "paper" and computer_choice == "paper":
            print(f"{computer_choice}")
            print("Draw!")
            print(f"Result: {player_one}-{counter_player_one} : {player_two}-{counter_player_two}")

        elif player_one_choice == "paper" and computer_choice == "scissors":
            print(f"{computer_choice}")
            print(f"Point for the {player_two}!")
            counter_player_two += 1
            print(f"Result: {player_one}-{counter_player_one} : {player_two}-{counter_player_two}")

        elif player_one_choice == "scissors" and computer_choice == "rock":
            print(f"{computer_choice}")
            print(f"Point for the {player_two}!")
            counter_player_two += 1
            print(f"Result: {player_one}-{counter_player_one} : {player_two}-{counter_player_two}")

        elif player_one_choice == "scissors" and computer_choice == "paper":
            print(f"{computer_choice}")
            print(f"Point for {player_one}!")
            counter_player_one += 1
            print(f"Result: {player_one}-{counter_player_one} : {player_two}-{counter_player_two}")

        elif player_one_choice == "scissors" and computer_choice == "scissors":
            print(f"{computer_choice}")
            print("Draw!")
            print(f"Result: {player_one}-{counter_player_one} : {player_two}-{counter_player_two}")

    if counter_player_one > counter_player_two:
        print(f"{player_one} Wins!")
    else:
        print(f"The {player_two} Wins!")
