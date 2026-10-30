#!/usr/bin/env python3
numbers = [2,8,9,48,8,22,-12,2]
new_numbers = []
for number in numbers:
    new_number = number + 2
    new_numbers.append(new_number)
print("Original array:", numbers)
print("New array:", new_numbers)