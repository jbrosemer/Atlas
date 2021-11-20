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
                print("CW")
                CW = False
                CCW = True
            else:
                print("CCW")

                CCW = False
                CW = True
        if CW:
            kit.servo[0].angle = (80)
        if CCW:
            kit.servo[0].angle = (93)
except KeyboardInterrupt:
    end = time.time()
    print("time of run: ", start-end)