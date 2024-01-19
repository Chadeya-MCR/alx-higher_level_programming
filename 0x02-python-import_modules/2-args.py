#!/usr/bin/python3
from sys import argv

# Get the number of arguments passed
num_args = len(argv) - 1

# Print the number of arguments passed to the sript
print("Number of argument{}: {}{}".format('' if num_args == 1 else 's', num_args, '' if num_args != 0 else '.'))

# Print the list of arguments passed to the script
if num_args > 0:
    print("Argument{}:".format('s' if num_args > 1 else ''))
    
    # Iterate through the arguments and print each of them
    for i in range(1, num_args + 1):
        print("{}: {}".format(i, argv[i]))
