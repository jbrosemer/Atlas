import cv2
# import servokit to have pi move servos
from adafruit_servokit import ServoKit
# there are 16 channels on the servo kit
kit = ServoKit(channels=16)
# capture "video" from default camera
#defines the Haar Cascades
cascades = "haarcascade_frontalface_default.xml"
video = cv2.VideoCapture(0)

# what is the width of the frame we are capturing
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

#States for FSM
#Sweep to find number of players
Sweep = True
Look = False
Lock = False
Tilt = False
Wait = False
#Soham's Classes
#Ethics HRI core class
#Probablistic Core
#ME 123



while True:

    # Sweep mode, I.E one initial sweep to count the number of players and find their locations.
    # THIS MODE WILL NEED TO BE TESTED WITH THE UNIT
    # MIGHT NOT BE INCLUDED IN THE END, BUT WOULD BE THE FASTEST WAY TO PLAY
    if Sweep:
        ret, frame = video.read()
        # once the initial sweep is finished go to Look mode automatically
        if:
            Sweep = False
            Look = True


    # Look mode, I.E. looking for one of the people counted to throw the ball to.
    if Look:
        ret, frame = video.read()
        # turn the main servo 360 degrees than return to 0.
        # so +360 degree then -360 degree turn

        # if a face is detected get out of sweep mode
        Look = False
        Lock = True


    if Lock:
        Lock = False
        Tilt = True



    if Tilt:
        Tilt = False
        Wait = True



    if Wait:
        Wait = False
        Look = True

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
