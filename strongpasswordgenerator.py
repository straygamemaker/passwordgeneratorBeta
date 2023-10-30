#random strong password generator

import random 

print("Welcome to the Strong Password Generator. ")

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?}{|+-_0123456789'

length = int(input("How many characters long does your password need to be? Please input a whole numebr. Enter: "))

print("Here are your passwords: ")

for num in range(1):
    passwords = ''
    for x in range(length):
        passwords += random.choice(characters)

print(passwords)
