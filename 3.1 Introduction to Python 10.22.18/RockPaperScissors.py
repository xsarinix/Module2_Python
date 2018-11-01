# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice " +str(options)+": ")
print()
print(f"Game on! ")

# Run Conditionals
while user_choice=="r" or "p" or "s"
    if user_choice=="r"
        print("You've chosen rock.")
        if computer_choice == "r"
            print("The computer has also chosen rock.")
            print("It's a tie! Pick again.")
        elif computer_choice == "p"
            print("The computer chose paper.")
            print("Paper covers rock.")
            print("YOU LOSE!")
        elif computer_choice=="s"
            print("The computer chose scissors.")
            print("Rock breaks scissors.")
            print("YOU WIN!")
    elif user_choice=="p"
        print("You've chosen paper.")
        if computer_choice=="r"
            print("The computer has chosen rock.")
            print("Paper covers rock.")
            print("YOU WIN!")
        elif computer_choice=="p"
            print("The computer has also chosen paper.")
            print("It's a tie! Pick again.")
        elif computer_choice=="s"
            print("The computer has chosen scissors.")
            print("Scissors cut paper.")
            print("YOU LOSE!")
    elif user_choice=="s"
        print("You've chosen scissors.")
        if computer_choice="r"
            print("The computer has chosen rock.")
            print("Rock breaks scissors.")
            print("YOU LOSE!")
        elif computer_choice="p"
            print("The computer has chosen paper.")
            print("Scissors cut paper.")
            print("YOU WIN!")
        elif computer_choice="s"
            print("The computer has also chosen scissors.")
            print("")
