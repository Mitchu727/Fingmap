import serial

while True:
    y_coordinate = float(input("Podaj współrzędną y:"))
    x_coordinate = float(input("Podaj współrzędną x:"))
    f = open('series2/' + (str(y_coordinate) + '_' + str(x_coordinate) + '.txt'), "w+")
    numerator = 0 
    arduino = serial.Serial('COM4', 9600)
    while (numerator < 1000):
        row = arduino.readline()
        if row:
            row = row.decode()
            data = row.split(",")
            if len(data) == 6:
                f.write(row[:-2])
                f.write("\n")
                print(numerator, row)
                numerator += 1
    print((y_coordinate, x_coordinate))
    arduino.close()
