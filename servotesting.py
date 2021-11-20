import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
CW = True
CCW = False
try:
    start = time.time()
    while True:
        if time.time()-start > 3:
            start = time.time()
            if CW:
                CW = False
                CCW = True
            else:
                CCW = False
                CW = True
        if CW:
            print("cw")
            kit.servo[0].angle = (76)
        if CCW:
            print("ccw")
            kit.servo[0].angle = (81)
except KeyboardInterrupt:
    end = time.time()
    print("time of run: ", start-end)