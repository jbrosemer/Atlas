import serial

if __name__ == "main":
    ser = serial.Serial('/dev/ttyACMO',9600, timeout = 1)
    ser.flush()

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)