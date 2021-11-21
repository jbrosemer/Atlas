import cv2
import time
import serial
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
#ser = serial.Serial('/dev/ttyUSB0', 9600)
Look = True
Lock = False
Drop = False
Wait = False
CW = True
CCW = False
cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
while Look:
    angle = 110
    angle2 = 90 + (90 - int(angle))
    kit.servo[1].angle = (int(angle))
    kit.servo[2].angle = (int(angle2))
    ret, frame = cap.read()

    # grayscale the captured frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        # flags = cv2.CV_HAAR_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    print("Found {0} faces!".format(len(faces)))
    if len(faces) > 0:
        #        self.faceTracking.aim(faces[0])
        Look = False
        Lock = True
    if CCW:
        if time.time() - start > 5.6:
            start = time.time()
            if CW:
                CW = False
                CCW = True
            else:
                CCW = False
                CW = True
    elif CW:
        if time.time() - start > 5:
            start = time.time()
            if CW:
                CW = False
                CCW = True
            else:
                CCW = False
                CW = True
    if CW:
        print("cw")
        kit.servo[0].angle = (87)
    elif CCW:
        print("ccw")
        kit.servo[0].angle = (78)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
while Lock:
    ret, frame = cap.read()

    # grayscale the captured frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        # flags = cv2.CV_HAAR_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if (2*x + w)/2 > (width/2+25):
            kit.servo[0].angle = (86)
        elif (2*x + w)/2 < (width/2-25):
            kit.servo[0].angle = (80)
        else:
            kit.servo[0].angle = (82)
            Drop = True
            Lock = False

while Drop:
    angle = 125
    angle2 = 90 + (90 - int(angle))
    kit.servo[1].angle = (int(angle))
    kit.servo[2].angle = (int(angle2))
    Wait = True
    Drop = False

while Wait:
    angle = 110
    angle2 = 90 + (90 - int(angle))
    kit.servo[1].angle = (int(angle))
    kit.servo[2].angle = (int(angle2))



