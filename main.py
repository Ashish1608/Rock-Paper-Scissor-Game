import random
from art import rock, paper, scissors


def result(user_option, computer_option):

    if user_option == computer_option:
        return "It's a draw!"

    else:
        if user_option == 2 and computer_option == 0:
            return "You lose."

        elif user_option == 0 and computer_option == 2:
            return "You win!"

        elif user_option > computer_option:
            return "You win!"

        elif user_option < computer_option:
            return "You lose."


options = [rock, paper, scissors]
option_names = ["rock", "paper", "scissor"]

user_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors: "))
computer_choice = random.randint(0, 2)

if (user_choice < 0) or (user_choice > 2):
    print("\nThis option is not available. Please provide valid input")

else:
    print(f"\nYou Chose: {option_names[user_choice]}")
    print(options[user_choice])
    print(f"Computer Chose: {option_names[computer_choice]}")
    print(options[computer_choice])

    print(result(user_choice, computer_choice))
