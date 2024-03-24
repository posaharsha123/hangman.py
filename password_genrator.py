import random
import string

while True:
    letters = list(string.ascii_uppercase + string.ascii_lowercase)
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    a = input("Enter your name: ")
    print(f"Hi {a}! Welcome to the password generator.")

    L = int(input("Enter how many letters you want: "))
    s = int(input("Enter how many special characters you want: "))
    n = int(input("Enter how many numbers you want: "))

    gate = ''
    for i in range(L):
        ga = random.choice(letters)
        gate += ga

    for i in range(s):
        pa = random.choice(special_characters)
        gate += pa

    for i in range(n):
        ba = random.choice(numbers)
        gate += ba

    print("Generated password:", gate)

    again = input("Do you want to generate another password? (yes/no): ")
    if again.lower() != 'yes':
        break
