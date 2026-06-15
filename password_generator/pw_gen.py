import string
import random

def generate_password(length, include_uppercase,\
                      include_num, include_special):
    if length < (include_uppercase + include_special + include_num):
        raise ValueError("PASSWORD LENGTH IS TOO SHORT FOR THE SPECIFIED CRITERIA")

    password =''

    if include_uppercase:
        password += random.choice(string.ascii_uppercase)
    if include_num:
        password += random.choice(string.digits)
    if include_special:
        password += random.choice(string.punctuation)
    
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_num:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    for _ in range(length - len(password)):
        password += random.choice(characters)

    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

def main():
    length = int(input('Enter password length: '))
    include_uppercase = input('Do you want to include Uppercase letters (y/n): ').lower()=='y'
    include_num = input('Do you want to include numbers (y/n): ').lower() == 'y'
    include_special = input('Do you want to include special characters (y/n): ').lower() == 'y'
    try:
        password = generate_password(length,include_uppercase,include_num, include_special)
        print(password)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()