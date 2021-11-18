import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
CW = True
CCW = False
try:
    start = time.time()
    while True:
        if time.time()-start > 2:
            start = time.time()
            if CW:
                print("here")
                CW = False
                CCW = True
            else:
                print("here2")

                CCW = False
                CW = True
        if CW:
            kit.servo[0].angle = (87)
        if CCW:
            kit.servo[0].angle = (97)
except KeyboardInterrupt:
    end = time.time()
    print("time of run: ", start-end)