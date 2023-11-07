import random

user_score = 0
computer_score = 0

while True:
    print("\nWelcome to Rock, Paper, Scissors!")
    print("---------------------------------\n")
    times = 0
    while times<5:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
    
        if user_choice in choices:
            print(f"You choise {user_choice}.")
            print(f"The computer chose {computer_choice}.")

            if user_choice == computer_choice:
                result = "It's a tie!"
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "scissors" and computer_choice == "paper") or \
                 (user_choice == "paper" and computer_choice == "rock"):
                 result = "You win!"
                 user_score += 1
            else:
                result = "Computer wins!"
                computer_score += 1

            print(result)
            print(f"Your Score: {user_score} - Computer Score: {computer_score}\n")
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.\n")
        times += 1

    if user_score>computer_score:
        print("You Won!")
    else:
        print("You Lost!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

    print("Thanks for playing!")
