## create a function the returns the user input of how many guesses should be allowed in the game
def set_turn_limit():
        while True:
            try:
                turn_limit = int(input("How many guesses do you want to have? For unlimited enter '0': "))
                return turn_limit
            except ValueError:
                print("Please enter an integer")

## create a function that returns the user input for minimum and maximum values of the range to be used in the game
def set_game_params():
    min = input
    while True:
        try:
            min = int(input("What lower bound do you want: "))
            break
        except ValueError:
            print("Please enter an integer")
    while True:
        try:
            max = int(input("What upper bound do you want: "))
            if max <= min:
                print("The upper bound must be greater than the lower bound")
                continue
            else:    
                break
        except ValueError:
            print("Please enter an integer")
    return min, max


##  create a function that returns a random value that is inside a given range
import random
def computer_select(min, max):
    computer_selection = random.randint(min,max)
    return computer_selection

## create a function that returns a user input. Ensure that the input is a integer
def user_guess():
    while True:
        try:
            user_input = int(input("What is your guess?: "))
            return user_input
        except ValueError:
            print("Please enter an integer")

## create a function that compares two numbers and prints a message based on if they are equal or if the second is lower or higher than the first. It should return True if there is a match otherwise false
def compare_numbers(user_input, computer_selection):
    if user_input == computer_selection:
        print("You guessed correctly")
        return True
    elif user_input < computer_selection:
        print(f"Your guess of {user_input} is too low")
        return False
    elif user_input > computer_selection:
        print(f"Your guess of {user_input} is too high")
        return False
    
## create a function that combines the 5 previous function into a single program, perhaps with some more text printouts that plays through the game from beginning to end.     

def game_function():
    print("Welcome to the game. You need to guess the number the computer has put in its memory.")
    print("Let's choose the conditions of the game")
    min, max = set_game_params()
    turn_limit = set_turn_limit()
    computer_selection = computer_select(min, max)
    turns = 1
    while turns <= turn_limit or turn_limit == 0:
        if compare_numbers(user_guess(), computer_selection):
            print(f"You guessed right in {turns} turns! Nice Job")
            break
        else:
            turns +=1
    print(f"The right answer was {computer_selection}")

if __name__ == "__main__":
    game_function()