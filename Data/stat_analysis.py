import matplotlib.pyplot as plt
import statistics
import csv


def statistify(distance):
    if len(distance) == 0:
        return "No data"
    else:
        return statistics.mean(distance), statistics.median(distance), statistics.variance(distance) 


coordinates = [[13.0, 10.0], [14.0, 10.0], [15.0, 10.0], [15.0, 11.0],
            [15.0, 12.0], [20.0, 5.0], [20.0, 10.0], [20.0, 15.0], [20.0, 20.0]]

for coordinates_pair in coordinates:
    offset = 0
    index = []
    idx = 0
    distance1 = []
    distance2 = []
    distance3 = []
    with open("standarized/" + str(coordinates_pair[0]) + "_" + str(coordinates_pair[1]) + ".txt", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 6 + offset:
                odczyt1 = float(row[1+offset])
                odczyt2 = float(row[3+offset])
                odczyt3 = float(row[5+offset])
                index.append(idx)
                if (odczyt1 < 35): distance1.append(odczyt1)
                if (odczyt2 < 35): distance2.append(odczyt2)
                if (odczyt3 < 35): distance3.append(odczyt3)
                idx += 1


    print(coordinates_pair)
    print(*statistify(distance1))
    print(*statistify(distance2))
    print(*statistify(distance3))



# axe1 = [0 for _ in range(len(distance1))]
# axe2 = [-1 for _ in range(len(distance2))]
# axe3 = [1 for _ in range(len(distance3))]
# plt.boxplot(distance1)
# plt.show()
# plt.plot(distance1, axe1, "r.")
# plt.plot(distance2, axe2, "g.")
# plt.plot(distance3, axe3, "b.")
# plt.show()
