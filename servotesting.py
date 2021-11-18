import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
CW = True
CCW = False
try:
    start = time.time()
    while True:
        print(str(round((time.time()-start)*10,1) % 17))
        if round((time.time()-start)*10, 1) % 17 == 1.0:
            print("here")
            if CW:
                CW = False
                CCW = True
            else:
                CCW = False
                CW = True
        if CW:
            kit.servo[0].angle = (80)
        if CCW:
            kit.servo[0].angle = (80)
except KeyboardInterrupt:
    end = time.time()
    print("time of run: ", start-end)