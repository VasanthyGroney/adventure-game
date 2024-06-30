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


