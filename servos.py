import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
while True:
    angle = input("enter the motor speed: ")
    kit.servo[0].angle = (int(angle))