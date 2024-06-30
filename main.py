def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest.")
    print("There are paths to your left and right.")
    first_choice()

def first_choice():
    print("\nDo you want to go left or right?")
    choice = input("Type 'left' or 'right': ").lower()

    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    else:
        print("Invalid choice. Please type 'left' or 'right'.")
        first_choice()
def left_path():
    print("\nYou walk down the left path and encounter a river.")
    print("Do you want to swim across or walk along the bank?")
    choice = input("Type 'swim' or 'walk': ").lower()

    if choice == 'swim':
        print("You swim across the river and reach the other side safely.")
        print("Congratulations! You found a hidden treasure!")
    elif choice == 'walk':
        print("You walk along the bank and find a bridge to cross the river.")
        print("On the other side, you find a small village.")
        village()
    else:
        print("Invalid choice. Please type 'swim' or 'walk'.")
        left_path()

def village():
    print("\nIn the village, you see a market and a tavern.")
    print("Do you want to visit the market or the tavern?")
    choice = input("Type 'market' or 'tavern': ").lower()

    if choice == 'market':
        print("You buy some supplies at the market and continue your adventure.")
    elif choice == 'tavern':
        print("You rest at the tavern and hear stories about hidden treasures in the forest.")
    else:
        print("Invalid choice. Please type 'market' or 'tavern'.")
        village()

def right_path():
    print("\nYou walk down the right path and encounter a wild animal.")
    print("Do you want to fight the animal or run away?")
    choice = input("Type 'fight' or 'run': ").lower()

    if choice == 'fight':
        print("You bravely fight the animal and win!")
        print("You find a mysterious cave behind the animal.")
        cave()
    elif choice == 'run':
        print("You run away safely and find yourself back at the start.")
        first_choice()
    else:
        print("Invalid choice. Please type 'fight' or 'run'.")
        right_path()



