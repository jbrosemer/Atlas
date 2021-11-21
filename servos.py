import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
start = 0
while True:
    angle = input("enter the motor speed: ")
    print(str(time.time()-start))
    start = time.time()
    kit.servo[1].angle = (int(angle))