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
                CW = True
                CCW = False
            else:
                print("CCW")

                CCW = True
                CW = False
        if CW:
            kit.servo[0].angle = (81)
        if CCW:
            kit.servo[0].angle = (92)
except KeyboardInterrupt:
    end = time.time()
    print("time of run: ", start-end)