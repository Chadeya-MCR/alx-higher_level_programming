def best_score(a_dictionary):
    if a_dictionary:
        # Find the key with the maximum value
        max_key = max(a_dictionary, key=a_dictionary.get)
        return max_key
    else:
        return None


if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))
