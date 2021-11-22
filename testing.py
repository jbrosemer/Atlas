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
FirstTime = True
LockFirstTime = True
CW = False
CCW = True
increment = 0
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS , 30)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
start = time.time()
try:
    while True:
        while Look:
            print('look')
            angle = 0
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
            if not FirstTime:
                if len(faces) > 0:
                    #        self.faceTracking.aim(faces[0])
                    increment += 1
                    if increment > 4:
                        Look = False
                        Lock = True
                        LockFirstTime = True
                else:
                    increment = 0
            else:
                FirstTime = False
                if len(faces) > 0:
                    #        self.faceTracking.aim(faces[0])
                    increment += 1
                else:
                    increment = 0

            if CCW:
                if time.time() - start > 15:
                    start = time.time()
                    if CW:
                        CW = False
                        CCW = True
                    else:
                        CCW = False
                        CW = True
            elif CW:
                if time.time() - start > 15:
                    start = time.time()
                    if CW:
                        CW = False
                        CCW = True
                    else:
                        CCW = False
                        CW = True
            if CW:
                print("cw")
                kit.servo[0].angle = 93
            elif CCW:
                print("ccw")
                kit.servo[0].angle = (87)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        while Lock:
            increment = 0
            print('lock')
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
            if LockFirstTime:
                locker = time.time()
                LockFirstTime = False
            else:
                if time.time()-locker > 2:
                    Look = True
                    Lock = False
            if len(faces) > 0:
                LockFirstTime = True
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                if (2*x + w)/2 > (width/2+30):
                    kit.servo[0].angle = (92)
                elif (2*x + w)/2 < (width/2-30):
                    kit.servo[0].angle = (87)
                else:
                    kit.servo[0].angle = (90)
                    Drop = True
                    Lock = False

        while Drop:
            kit.servo[0].angle = (90)
            print('drop')
            angle = 30
            angle2 = 90 + (90 - int(angle))
            kit.servo[1].angle = (int(angle))
            kit.servo[2].angle = (int(angle2))
            time.sleep(5)
            Wait = True
            Drop = False

        while Wait:
            increment = 0
            print('wait')
            angle = 0
            angle2 = 90 + (90 - int(angle))
            kit.servo[1].angle = (int(angle))
            kit.servo[2].angle = (int(angle2))
            time.sleep(5)
            Look = True
            Wait = False
            FirstTime = True
            if CW:
                CCW = True
                CW = False
            else:
                CW = True
                CCW = False
except KeyboardInterrupt:
    kit.servo[0].angle = (90)


