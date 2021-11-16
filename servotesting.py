from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)

servo=kit.servo[1]
while True:
	t1=int(input('Enter servo angle:'))
	servo.angle = t1
	time.sleep(10)
	servo.angle = 90

#t1_servo= kit.servo[0]
#t2_servo= kit.servo[1]

#while True:
#    t1=int(input('Enter servo angle for servo 1: '))
#    t1_servo.angle=t1
#     t2=int(input('Enter servo angle for servo 2: '))
#     t2_servo.angle=t2
    
