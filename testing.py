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
ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.flush()
try:
    while True:
        # look state to find a person to toss to
        while Look:
            print('look')
            # resets ball ropper just in case not already
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
            #look for faces and draw a box around them
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # prints number of faces found
            print("Found {0} faces!".format(len(faces)))
            #waits to find a "face" for a longer duration of time
            if not FirstTime:
                # if it found a face
                if len(faces) > 0:
                    #        self.faceTracking.aim(faces[0])
                    #increment
                    increment += 1
                    #if face has been on screen for a while
                    if increment > 4:
                        #move to lock state
                        Look = False
                        Lock = True
                        #were going to lock for the first time
                        LockFirstTime = True
                # if no faces are found reset face timer
                else:
                    increment = 0
            else:
                FirstTime = False
                #if finding a face keep incrementing until 5
                if len(faces) > 0:
                    #        self.faceTracking.aim(faces[0])
                    increment += 1
                else:
                    increment = 0
            #turn ccw for 15 seconds
            if CCW:
                if time.time() - start > 15:
                    start = time.time()
                    if CW:
                        CW = False
                        CCW = True
                    else:
                        CCW = False
                        CW = True
            #turn CW for 15 seconds
            elif CW:
                if time.time() - start > 15:
                    start = time.time()
                    if CW:
                        CW = True
                        CCW = False
                    else:
                        CCW = True
                        CW = False
            #defines CW speed and CCW speed
            if CW:
                print("cw")
                kit.servo[0].angle = 93
            elif CCW:
                print("ccw")
                kit.servo[0].angle = (87)
            #break if cant find camera
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        #lock state to lock onto a face
        while Lock:
            #reset increment if in Lock
            increment = 0
            print('lock')
            #re-read camera information
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
            #operates on the same basis as look, if it detects a face in the midde of the screen for a while it launches
            #otherwise it goes back to look
            if LockFirstTime:
                locker = time.time()
                LockFirstTime = False
            # if it isn't the first time and some time has passed without a face go back to look
            else:
                if time.time()-locker > 2:
                    Look = True
                    Lock = False

            if len(faces) > 0:
                LockFirstTime = True
            # tries to center on the face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                if (2*x + w)/2 > (width/2+30):
                    kit.servo[0].angle = (92)
                elif (2*x + w)/2 < (width/2-30):
                    kit.servo[0].angle = (87)
                else:
                # if face is somewhat centered stop moving and go to drop state
                    kit.servo[0].angle = (90)
                    Drop = True
                    Lock = False
        #drop ball statex`
        while Drop:
            # make sure revolving motor is stopped
            kit.servo[0].angle = (90)
            print('drop')
            #drop the ball set both servo angles
            angle = 30
            angle2 = 90 + (90 - int(angle))
            # set those angles
            kit.servo[1].angle = (int(angle))
            kit.servo[2].angle = (int(angle2))
            time.sleep(1)
            #reset dropped ball angles
            angle = 0
            angle2 = 90 + (90 - int(angle))
            kit.servo[1].angle = (int(angle))
            kit.servo[2].angle = (int(angle2))
            # go to wait state to wait for ball to come back
            Wait = True
            Drop = False
        # wait for ball to return
        while Wait:
            increment = 0
            print('wait')
            # reset ball dropper angles
            angle = 0
            angle2 = 90 + (90 - int(angle))
            kit.servo[1].angle = (int(angle))
            kit.servo[2].angle = (int(angle2))
            time.sleep(1)
            # go to look state
            read_serial = ser.readline()
            read_serial = read_serial.decode("utf-8")
            strs = read_serial.split(" ")
            # read lidar data and go to look state if a ball is found
            if len(strs) > 3:
                if int(strs[5]) < 40:
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


