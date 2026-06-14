import random
'''
LOOP
 Ask: roll the dice?
 if user enters "yes":
     roll the dice
     display the result
 if the user enters "no":
    print thank you message
    terminate the program
 else:
    print invalid input message
    repeat the loop
'''
playing = True
while playing:
    a = input("Enter 'yes' or 'no' to roll the dice: ")
    if(a == "yes" or a=="Yes" or a=="YES"):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')
    elif(a=="no" or a=="No"or a=="NO"):
        print("Thanks for playing!")
        break
    else:
        print("Invalid Input please enter the choice again")
    