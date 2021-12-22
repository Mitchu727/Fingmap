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


def get_data(directory, encode, **kwargs):
    data_dictionary = get_dictionary(directory)
    data = []
    if 'column' in kwargs.keys():
        data_dictionary = filter_dictionary_column(kwargs['column'], data_dictionary)
        data_dictionary = sort_dictionary(data_dictionary)
    if 'row' in kwargs.keys():
        data_dictionary = filter_dictionary_row(kwargs['row'], data_dictionary)
        data_dictionary = sort_dictionary(data_dictionary)
    for measurement in data_dictionary:
        data += get_measurement(directory, measurement, data_dictionary, encode)
    return data, data_dictionary


def filter_dictionary_column(column, dictionary):
    new_dictionary = {}
    for key, value in dictionary.items():
        if float(key.split('_')[1]) == column:
            new_dictionary[key] = value
    return new_dictionary


def filter_dictionary_row(row, dictionary):
    new_dictionary = {}
    for key, value in dictionary.items():
        if float(key.split('_')[0]) == row:
            new_dictionary[key] = value
    return new_dictionary


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
        print(class_index)
        numerator = 0
        for element in class_vector[class_index]:
            print(numerator)
            classification_array[class_index][predict(element[0], *predict_params)-1] += 1
            numerator = numerator + 1
    return classification_array


def create_classification_heatmap(classification_array, data_dictionary):
    fig, ax = plt.subplots()
    fig.set_figheight(fig.get_figheight() * 4)
    fig.set_figwidth(fig.get_figwidth() * 4)
    ax.imshow(classification_array)
    ax.set_xticks(np.arange(len(data_dictionary)))
    ax.set_yticks(np.arange(len(data_dictionary)))
    ax.set_xticklabels(data_dictionary)
    ax.set_yticklabels(data_dictionary)
    for i in range(len(data_dictionary)):
        for j in range(len(data_dictionary)):
            ax.text(j, i, classification_array[i, j],
                    ha="center", va="center", color="w")


def create_class_heatmap(class_name, data_dictionary, classification_array, inverse=False):
    """
    dla inverse = True, pokazuje do jakich klas został zakwalifikowany obiekt klasy tytułowej
    dla inverse = False, pokazuje jakie klasy zostały zakwalifikowane jako obiekt klasy tytułowej
    """
    if not inverse:
        create_heatmap(class_name, data_dictionary, classification_array[data_dictionary[class_name]-1])
    else:
        create_heatmap(class_name, data_dictionary, classification_array[:, data_dictionary[class_name]-1])


def create_heatmap(class_name, data_dictionary, data_array):
    fig, ax = plt.subplots()
    x_axis, y_axis = get_dictionary_axes(data_dictionary)
    data_array_reshaped = data_array.reshape(len(y_axis), len(x_axis))
    im = ax.imshow(data_array_reshaped)
    ax.set_xticks(np.arange(len(x_axis)))
    ax.set_yticks(np.arange(len(y_axis)))
    ax.set_xticklabels(x_axis)
    ax.set_yticklabels(y_axis)
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("", rotation=-90, va="bottom")
    ax.set_title(class_name)
    for i in range(len(y_axis)):
        for j in range(len(x_axis)):
            ax.text(j, i, f"{data_array_reshaped[i, j]:.03f}",
                    ha="center", va="center", color="w")


def calculate_recall(classification_array):
    """
    Recall is the percentage of all cat images in the dev (or test) set that it correctly
    labeled as a cat.(definition from Machine Learning Yearning by Andrew NG)
    """
    recall_list = np.zeros(len(classification_array))
    for class_index in range(len(classification_array)):
        recall_list[class_index] = 100*classification_array[class_index][class_index]/classification_array[class_index].sum()
    return recall_list


def calculate_precision(classification_array):
    """
    Precision  is the fraction of images in the dev (or test) set it labeled as cats that
    really are cats.(definition from Machine Learning Yearning by Andrew NG)
    """
    precision_list = np.zeros(len(classification_array))
    for class_index in range(len(classification_array)):
        if classification_array[:, class_index].sum() == 0:
            precision_list[class_index] = -100
        else:
            precision_list[class_index] = 100*classification_array[:, class_index][class_index]/classification_array[:, class_index].sum()
    return precision_list