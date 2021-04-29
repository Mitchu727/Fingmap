import os
import csv
import numpy as np
import matplotlib.pyplot as plt


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
    return sort_dictionary(dictionary)


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


def sort_dictionary(dictionary):
    y_axis = []
    x_axis = []
    for element in dictionary.keys():
        y, x = element.split('_')
        if float(y) not in y_axis:
            y_axis.append(float(y))
        if float(x) not in x_axis:
            x_axis.append(float(x))
    x_axis.sort()
    y_axis.sort()
    y_axis.reverse()
    numerator = 1
    new_dictionary = {}
    for y in y_axis:
        for x in x_axis:
            new_dictionary[str(y) + "_" + str(x)] = numerator
            numerator += 1
    return new_dictionary


def get_dictionary_axes(dictionary):
    y_axis = []
    x_axis = []
    for element in dictionary.keys():
        y, x = element.split('_')
        if float(y) not in y_axis:
            y_axis.append(float(y))
        if float(x) not in x_axis:
            x_axis.append(float(x))
    return x_axis, y_axis


def test(class_vector, predict, predict_params):
    classification_array = np.zeros((len(class_vector), len(class_vector)))
    for class_index in range(len(class_vector)):
        for element in class_vector[class_index]:
            classification_array[class_index][predict(element[0], *predict_params)-1] += 1
    return classification_array


def create_heatmap(class_name, data_dictionary, classification_array, inverse=False):
    """
    dla inverse = True, pokazuje do jakich klas został zakwalifikowany obiekt klasy tytułowej
    dla inverse = False, pokazuje jakie klasy zostały zakwalifikowane jako obiekt klasy tytułowej
    """
    fig, ax = plt.subplots()
    x_axis, y_axis = get_dictionary_axes(data_dictionary)
    if not inverse:
        im = ax.imshow(classification_array[data_dictionary[class_name]-1].reshape(len(y_axis), len(x_axis)))
    else:
        im = ax.imshow(classification_array[:, data_dictionary[class_name]-1].reshape(len(y_axis), len(x_axis)))
    ax.set_xticks(np.arange(len(x_axis)))
    ax.set_yticks(np.arange(len(y_axis)))
    ax.set_xticklabels(x_axis)
    ax.set_yticklabels(y_axis)
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("", rotation=-90, va="bottom")
    ax.set_title(class_name)
