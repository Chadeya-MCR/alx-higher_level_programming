#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_set = set(my_list)  # Convert the list to a set to keep only unique elements
    return sum(unique_set)

if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))

