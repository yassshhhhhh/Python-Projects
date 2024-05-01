import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']
print("Welcome to Rock, Paper Scissors, Let's Play!")


while True:
    user_input = input("Type Rock/Paper/scissors or Q to Quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    Nums = random.randint(0, 2)
    # 0 = Rock, 1 = Paper, 2 = Scissors

    computer_pick = options[Nums]
    print("Computer picks", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a tie.")
    else:
        print("You lost!")
        computer_wins += 1



print("Computer won", computer_wins, "times.")
print("You won", user_wins, "times.")
print("Goodbye!")