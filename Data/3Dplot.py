from mpl_toolkits import mplot3d
import numpy as np
import csv
import matplotlib.pyplot as plt

def encode(name):
    if name == [20.0, 10.0]:
        return 1
    elif name == [20.0, 15.0]:
        return 2
    elif name == [20.0, 20.0]:
        return 3
    elif name == [20.0, 5.0]:
        return 4
    else:
        raise Exception("Encoding error")

def control(reading):
    return min(reading, 50)

offset = 0
def get_data(first_parameter, second_parameter):
    sample_data = []
    with open("standarized/" + str(first_parameter) + "_" + str(second_parameter) + ".txt", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 6 + offset:
                odczyt1 = float(row[1+offset])
                odczyt2 = float(row[3+offset])
                odczyt3 = float(row[5+offset])
                sample_data.append([encode([first_parameter, second_parameter]), 
                                    np.array([control(odczyt1), control(odczyt2), control(odczyt3)])])
    return sample_data


def get_feature(data, feature, wine_class=None):
    return [record[1][feature] for record in data if not wine_class or (record[0] == wine_class)]

ax = plt.axes(projection='3d')

set1 = get_data(20.0, 5.0)
xline1 = get_feature(set1, 0)
yline1 = get_feature(set1, 1)
zline1 = get_feature(set1, 2)
ax.scatter3D(xline1, yline1, zline1, c='orange', label='Współrzędne (20, 5)')



set1 = get_data(20.0, 10.0)
xline1 = get_feature(set1, 0)
yline1 = get_feature(set1, 1)
zline1 = get_feature(set1, 2)
ax.scatter3D(xline1, yline1, zline1, c='red', label='Współrzędne (20, 10)')

set2 = get_data(20.0, 15.0)
xline2 = get_feature(set2, 0)
yline2 = get_feature(set2, 1)
zline2 = get_feature(set2, 2)
ax.scatter3D(xline2, yline2, zline2, c='blue', label='Współrzędne (20, 15)')

set3 = get_data(20.0, 20.0)
xline3 = get_feature(set3, 0)
yline3 = get_feature(set3, 1)
zline3 = get_feature(set3, 2)
ax.scatter3D(xline3, yline3, zline3, c='green', label='Współrzędne (20, 20)')
plt.legend()
plt.show()
 
