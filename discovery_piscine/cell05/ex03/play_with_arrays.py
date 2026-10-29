#!/usr/bin/env python3
numbers = [2,8,9,48,8,22,-12,2]
new_numbers = []
for number in numbers:
    if number > 5:
        result = number + 2
        if result not in new_numbers:
            new_numbers.append(result)
print(numbers)
print(set(new_numbers))