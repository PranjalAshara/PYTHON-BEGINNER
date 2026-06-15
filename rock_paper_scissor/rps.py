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

emojis = {
    'r':'🪨',
    'p':'📃',
    's':'✂️'
}
choices = ('r','p','s')

while True:
    user_choice: str = input("Rock Paper Scissor? (r/p/s): ").lower()
    if(user_choice not in choices):
        print("Invalid Input, please enter a valid choice")
        continue

    computer_choice = random.choice(choices)

    print(f'You chose: {user_choice} {emojis[user_choice]}')
    print(f'Computer chose: {computer_choice} {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie!')

    elif(
        (user_choice =='r' and computer_choice =='s')
        or (user_choice=='p' and computer_choice=='r')
        or (user_choice=='s' and computer_choice=='p')):
        print('You win!')

    else:
        print("Computer wins!")

    play = input('Wanna play Rock, Paper, Scissors?(y/n): ').lower()
    if play not in ('y','n'):
        print("Please enter 'y' or 'n' ")
    if(play == 'y'):
        continue
    if(play == 'n'):
        print("Maybe we'll play next time")
        break