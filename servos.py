import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
start = 0
try:
    while True:
        angle = input("enter the motor speed: ")
        angle2 = 90 + (90 - int(angle))
        print(str(time.time()-start))
        start = time.time()
        kit.servo[1].angle = (int(angle))
        kit.servo[2].angle = (int(angle2))
except KeyboardInterrupt:
    angle = 0
    angle2 = 180 - int(angle)
    kit.servo[1].angle = (int(angle))
    kit.servo[2].angle = (int(angle2))