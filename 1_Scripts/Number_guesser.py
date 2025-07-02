# Import library
import random

# Function to set lower and higher bounds
def bounds():
    try:
        lower = int(input("Please enter the lower bound: "))
        higher = int(input("Please enter then higher bound: "))
        if lower != higher:
            if lower < higher:
                return lower, higher
            else:
                print("The lower bound MUST BE LESS than the higher bound!")
        else:
            print("The lower and higher bounds MUST be different!")
    except:
        print("Please set the bounds as integers.")
        
# Function to set the number of guesses
def guesses():
    try:
        number_guesses = int(input("Please enter the number of guesses you wish to have: "))
    except:
        print("Please set the number of guesses as an integer")
    else:
        if number_guesses < 0:
            print("Please select a POSTIVE number of guesses.")
        else:
            return number_guesses

# Number guessing game function
def guessing_game():
    lower, higher = bounds()
    random_number = random.randint(lower, higher)
    total_guesses = guesses()
    passed_turns = 0
    for turn in range(total_guesses):
        passed_turns += 1
        turns_left = total_guesses - passed_turns
        try:
            guess = int(input("Please enter your guess: "))
        except: 
            print("Your guess MUST be an integer!")
        if passed_turns < total_guesses:
            if guess == random_number:
                print("You've guessed the number!!!")
                break
            else:
                if guess < random_number:
                    print("Not quite! Try a little higher. You have ", turns_left, "turns left.")
                else:
                    print("Not quite! Try a little lower. You have ", turns_left, "turns left.")
        else:
            print("You've run out of guesses!")
            
        
    
    
    
    
    
