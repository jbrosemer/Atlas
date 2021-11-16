import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.flush()

while True:
    read_serial = ser.readline()
    read_serial = read_serial.decode("utf-8")
    strs = read_serial.split(" ")
    print(strs[4])
    print(read_serial)
