import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
start = 0
while True:
    angle = input("enter the motor speed: ")
    angle2 = input("enter second motor")
    print(str(time.time()-start))
    start = time.time()
    kit.servo[1].angle = (int(angle))
    kit.servo[2].angle = (int(angle2))