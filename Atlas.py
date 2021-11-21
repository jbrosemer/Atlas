import cv2
import time
import serial
from faceTracking import FaceTracking
from adafruit_servokit import ServoKit

class Atlas:
    def __init__(self):
        kit = ServoKit(channels=16)
        ser = serial.Serial('/dev/ttyUSB0', 9600)
        self.faceTracking = FaceTracking()
        self.atlas = kit.servo[0]
        self.roller1 = kit.servo[1]
        self.roller2 = kit.servo[2]
        self.cam = kit.servo[3]
        self.start = "Sweep"
        self.stateHandlers = {
            "Sweep" :  self.Sweep, 
            "Look"  :  self.Look,
            "Lock"  :  self.Lock, 
            "Wait"  :  self.Wait
        }

        # save servo rotation for each player
        self.player_pos = []

    def run(self):
        transition = self.stateHandlers[self.start]
        while True:
            next, cargo = transition(cargo)
            transition = self.stateHandlers[next]

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def Sweep(self):
        print("Sweep")
        # period T for continuous servo? - to stop sweeping
        trajectory = []
        while True: 
            self.atlas.throttle = 1.0
            trajectory.append((time.time(),self.atlas.throttle))
            faces = self.faceTracking.detect()

            if len(faces)>0:
                trajectory += self.faceTracking.aim(faces[0])
                self.atlas.throttle = 1.0
                trajectory.append((time.time(),self.atlas.throttle))
                    
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break

        ts = trajectory[0][0]
        dir = trajectory[0][1]
        pos = 0

        for pt in trajectory[1:]:
            if pt[1] != 0.0:
                pos += dir*(pt[0]-ts)
                ts = pt[0]
                dir = pt[1]
            else:
                self.player_pos.append(pos)
                pos = 0 

        return "Look"  

    def Look(self):
        print("Look")
        while True:
            for pos in self.player_pos:
                self.atlas.throttle = 1.0
                time.sleep(pos)
                self.atlas.throttle = 0.0

                faces = self.faceTracking.detect()
                if len(faces)>0:
                    self.faceTracking.aim(faces[0])
                    return "Lock"

                if cv2.waitKey(1) & 0xFF == ord('s'):
                    break

    def Lock(self):
        print("Lock")
        self.roller1.angle = 70
        self.roller2.angle = 70

        time.sleep(1000)

        self.roller1.angle = 0
        self.roller2.angle = 0

        return "Wait"

    def Wait(self):

        print("Wait")
