import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
try:
    start = time.time()
    while True:
        kit.servo[0].angle = (100)
except KeyboardInterrupt:
    end = time.time()
    print("time of run: ", start-end)