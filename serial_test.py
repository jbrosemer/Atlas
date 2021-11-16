from serial import Serial

ser = Serial('/dev/ttyUSB0', 9600)
ser.flush()

while True:
    read_serial = ser.readline()
    read_serial = read_serial.decode("utf-8")
    print(read_serial)
    