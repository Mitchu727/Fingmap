import os


def get_dictionary(directory):
    numerator = 1
    dictionary = {}
    for filename in os.listdir(directory):
        dictionary[str(filename[:-4])] = numerator
        numerator += 1
    return dictionary
