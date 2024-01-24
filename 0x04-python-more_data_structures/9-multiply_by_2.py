def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict


# Test the function
if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    new_dict = multiply_by_2(a_dictionary)

    for key, value in a_dictionary.items():
        print(f"{key}: {value}")
    print("--")
    for key, value in new_dict.items():
        print(f"{key}: {value}")
