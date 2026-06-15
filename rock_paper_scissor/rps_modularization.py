"""
In order to make the code more readable and modular
we
1) Divide the program into several function 
2) Avoid DRY(Don't Repeat Yourself)
"""

import random
"""
ask the user to make a choice
if the choice is invalid
print error
let the computer make choice
print choices(emojis)
determine winner
ask the usere if they want to continue
if not
terminate
"""
# use dictionary for key value pairs key -> value
#eg) 'r' -> 'rock(🪨)'


ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'
emojis = {
    ROCK:'🪨',
    PAPER:'📃',
    SCISSOR:'✂️'
}
choices = tuple((emojis.keys()))

def get_user_choice():
    while True:
        user_choice: str = input("Rock Paper Scissor? (r/p/s): ").lower()
        if(user_choice not in choices):
            print("Invalid Input, please enter a valid choice")
        else:
            return user_choice

def display_choices(user_choice,computer_choice):
    print(f'You chose: {user_choice} {emojis[user_choice]}')
    print(f'Computer chose: {computer_choice} {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')

    elif(
        (user_choice ==ROCK and computer_choice ==SCISSOR)
        or (user_choice==PAPER and computer_choice==ROCK)
        or (user_choice==SCISSOR and computer_choice==PAPER)):
        print('You win!')

    else:
        print("Computer wins!")

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice,computer_choice)

        determine_winner(user_choice,computer_choice)

        play = input('Wanna play Rock, Paper, Scissors?(y/n): ').lower()
        if play not in ('y','n'):
            print("Please enter 'y' or 'n' ")
        if(play == 'y'):
            continue
        if(play == 'n'):
            print("Maybe we'll play next time")
            break
        
play_game()

