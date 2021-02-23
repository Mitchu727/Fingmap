import serial
arduino = serial.Serial('COM4', 9600)
while True: print(arduino.readline().decode())