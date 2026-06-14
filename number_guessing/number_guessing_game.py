import random
"""
Generate a random number
LOOP
ask user to enter a random number
if not valid number
    print invalid input message
if number < guess
    print too low
if number > guess
    print too high
else
    print well done
"""

rand_int = random.randint(1,100)
print("Guess the number between 1 to 100")

while True:
    input_number = input("Enter number: ")
    if(input_number.isdigit()):
        input_number = int(input_number)
        if(rand_int < input_number):
            print("Lower than ",input_number)
        elif(rand_int > input_number):
            print("Greater than",input_number)
        else:
            print("Well done! You guessed the number")
            break
    else:
        print("Invalid input, please enter a valid number")
        break