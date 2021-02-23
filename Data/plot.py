import matplotlib.pyplot as plt
import statistics
import csv

offset = 0
index = []
idx = 0
distance1 = []
distance2 = []
distance3 = []
with open("standarized/15.0_10.0.txt", newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) == 6 + offset:
            odczyt1 = float(row[1+offset])
            odczyt2 = float(row[3+offset])
            odczyt3 = float(row[5+offset])
            index.append(idx)
            distance1.append(odczyt1)
            distance2.append(odczyt2)
            distance3.append(odczyt3)
            idx += 1


plt.plot(index, distance1, "r.")
plt.plot(index, distance2, "g.")
plt.plot(index, distance3, "b.")
plt.show()


# axe1 = [0 for _ in range(len(distance1))]
# axe2 = [-1 for _ in range(len(distance2))]
# axe3 = [1 for _ in range(len(distance3))]
# plt.boxplot(distance1)
# plt.show()
# plt.plot(distance1, axe1, "r.")
# plt.plot(distance2, axe2, "g.")
# plt.plot(distance3, axe3, "b.")
# plt.show()
