import os
import csv
import numpy as np


def control(reading):
    return min(reading, 50)

def encode(number, data_dictionary):
    vector = -np.ones(len(data_dictionary))
    vector[number-1] = 1
    return vector

def decode(vector):
    return np.argmax(vector) + 1


def get_dictionary(directory):
    numerator = 1
    dictionary = {}
    for filename in os.listdir(directory):
        dictionary[str(filename[:-4])] = numerator
        numerator += 1
    return dictionary


def get_measurement(directory, measurement, data_dictionary, encode):
    offset = 0
    sample_data = []
    with open(directory + "/" + measurement + ".txt", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 6 + offset:
                odczyt1 = float(row[1+offset])
                odczyt2 = float(row[3+offset])
                odczyt3 = float(row[5+offset])
                sample_data.append([np.array([control(odczyt1), control(odczyt2), control(odczyt3)]),
                                    encode(data_dictionary[measurement], data_dictionary)])
    return sample_data


def get_data(directory, encode):
    data_dictionary = get_dictionary(directory)
    data = []
    for measurement in data_dictionary:
        data += get_measurement(directory, measurement, data_dictionary, encode)
    return data, data_dictionary


def split_into_sets(train_test_ratio, data):
    np.random.shuffle(data)
    train_set_size = int(train_test_ratio*len(data))
    test_set_size = len(data) - train_set_size
    train_set = data[:train_set_size]
    test_set = data[-test_set_size:]
    return train_set, test_set


def split_into_classes(data, data_dictionary, decode):
    class_vector = [[] for element in data_dictionary]
    for row in data:
        class_vector[decode(row[1])-1].append(row)
    return class_vector



# data, data_dictionary = get_data("series3", encode)