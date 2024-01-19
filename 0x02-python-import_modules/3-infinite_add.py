#!/usr/bin/python3
from sys import argv

# Extract command-line arguments (excluding the script name)
arguments = argv[1:]

# Initialize the sum to 0
sum_result = 0

# Add up all the arguments
for arg in arguments:
    sum_result += int(arg)

# Print the result
print(sum_result)

