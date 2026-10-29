#!/usr/bin/env python3
user_input = input("Enter a number less than 25\n")

if user_input.isnumeric():
    number = int(user_input)
    if number > 25:
        print("Error")
    else:
        while number <= 25:
            print(f"inside the loop, my variable is {number}")
            number +=1