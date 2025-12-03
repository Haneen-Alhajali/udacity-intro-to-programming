import time
import random


# This function prints a message and waits a little
def print_pause(message):
    print(message)
    time.sleep(1)


# This function is used to make sure the player enters a correct choice
def get_choice(prompt, options):
    answer = input(prompt)
    while answer not in options:
        answer = input("Please choose a valid option: ")
    return answer


# When the player goes to the cave
def cave(inventory, enemy):
    print_pause("You walk slowly into the dark cave...")
    if "sword" not in inventory:
        print_pause("You find an old sword on the ground.")
        inventory.append("sword")
        print_pause("You take the sword with you.")
    else:
        print_pause("The cave is empty. You already took the sword.")
    print_pause("You go back to the field.")
    field(inventory, enemy)


# When the player goes to the house
def house(inventory, enemy):
    print_pause("You walk toward the creepy house...")
    print_pause(f"A {enemy} jumps out in front of you!")
    print_pause("What will you do?")

    choice = get_choice("Enter 1 to fight, or 2 to run away: ", ["1", "2"])

    if choice == "1":
        fight(inventory, enemy)
    else:
        print_pause("You run back to the field.")
        field(inventory, enemy)


# Fight scene
def fight(inventory, enemy):
    if "sword" in inventory:
        print_pause("You use your sword to fight!")
        print_pause(f"You defeat the {enemy}!")
        print_pause("You win! Good job.")
    else:
        print_pause("You try to fight with your hands...")
        print_pause(f"But the {enemy} is too strong.")
        print_pause("You lose the game.")
    play_again()


# Main field where the story starts
def field(inventory, enemy):
    print_pause("You are standing in a quiet, dark field.")
    print_pause("There is a small house in front of you.")
    print_pause("There is also a cave on your right.")

    choice = get_choice(
        "Enter 1 to go to the house, or 2 to go to the cave: ", ["1", "2"]
    )

    if choice == "1":
        house(inventory, enemy)
    else:
        cave(inventory, enemy)


# Ask the player if they want to play again
def play_again():
    again = get_choice("Do you want to play again? (y/n): ", ["y", "n"])
    if again == "y":
        print_pause("Restarting the game...")
        play_game()
    else:
        print_pause("Thanks for playing! Goodbye.")


# Game start
def play_game():
    enemy = random.choice(["ghost", "monster", "witch", "zombie", "Dragon"])
    inventory = []
    field(inventory, enemy)


play_game()
