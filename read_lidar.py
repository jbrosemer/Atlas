import serial
import time
from datetime import datetime
import os

ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.flush()

start = time.time()
with open(os.path.join(os.getcwd(),"logs", datetime.strftime(datetime.now(), "%d_%m_%Y_%H:%M:%S_logs")),'w') as f:
    while True:
        read_serial = ser.readline()
        read_serial = read_serial.decode("utf-8")
        strs = read_serial.split(" ")
        if len(strs) > 3:
            lidar = int(strs[5])
            time = time.time()-start
            if lidar < 40:
                print("Ball!")
                f.write(f"{time:.2f}, {lidar}\n")
            else:
                print(read_serial)

