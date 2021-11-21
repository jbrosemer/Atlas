import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
CW = True
CCW = False
try:
    start = time.time()
    while True:
        if CCW:
            if time.time()-start > 5.6:
                start = time.time()
                if CW:
                    CW = False
                    CCW = True
                else:
                    CCW = False
                    CW = True
        elif CW:
            if time.time()-start > 9:
                start = time.time()
                if CW:
                    CW = False
                    CCW = True
                else:
                    CCW = False
                    CW = True
        if CW:
            print("cw")
            kit.servo[0].angle = (94)
        elif CCW:
            print("ccw")
            kit.servo[0].angle = (86)
except KeyboardInterrupt:
    end = time.time()
    print("time of run: ", start-end)