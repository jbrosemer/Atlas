import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
start = 0
prevangle = 0
while True:
    prevangle = angle
    angle = input("enter the motor speed: ")
    angle2 = 90 + (90 - int(angle))
    print(str(time.time()-start))
    start = time.time()
    if prevangle != angle:
        kit.servo[1].angle = (int(angle))
        kit.servo[2].angle = (int(angle2))