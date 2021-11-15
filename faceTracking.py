import cv2
import time
# from adafruit_servokit import ServoKit

class FaceTracking():
    def __init__(self):
        cascPath = "haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(cascPath)

        self.cap = cv2.VideoCapture(0)
        # sets the fps of the video capturing to 15
        self.cap.set(cv2.CAP_PROP_FPS , 15)
        self.frame_w = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)/2


    def detect(self):
        ret, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize=(30,30)
        )

        return faces

    def aim(self, face):
        x = face[0]
        # y = face[1]
        w = face[2]
        # h = face[3]  

        box_mid = 2*x+w
        frame_mid = self.frame_w/2
        threshold = 25

        aiming = False
        micro_trajectory = []

        while not aiming:

            if box_mid > frame_mid + threshold:
                self.servo.throttle = 1.0
            elif box_mid < frame_mid - threshold:
                self.servo.throttle = -1.0
            else:
                self.servo.throttle = 0.0
                aiming = True

            micro_trajectory.append((time.time(),self.servo.throttle))
        
        return micro_trajectory
