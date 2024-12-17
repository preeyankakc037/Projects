#This is a Dice rolling Game

import random  

def roll_dice():
    return random.randint(1,6)
    # Python's random.randint(1,6) to generate a random number between 1 and 6.

def dice_game():
    print("Welcome to the Dice rolling game!")
    while True:
        # while is a looping construct in Python that keeps running as long as the condition is True.
        # True is a Boolean value in Python that is always considered "true."
        #This means the block of code inside the while will keep running forever, or until the program encounters a break.
        user_input=input("\n Type 'roll' to roll the dice or 'quit' to exit:" ).lower()
        

        if user_input=='roll':
            dice_result=roll_dice()
            print(f'You rolled a {dice_result}!')
        elif user_input=='quit':
            print("Thanks for playing!  Goodbye!")
            break
        else :
            print("Invalid input. Please type 'roll' or 'quit'.")

#Run the Game 
dice_game()