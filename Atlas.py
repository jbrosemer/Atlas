import cv2

cascades = "haarcascade_frontalface_default.xml"
video = cv2.VideoCapture(0)

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



while Sweep:
    if(Sweep):

        Sweep = False
        Look = True
    if(Look):
        Look = False
        Lock = True
    if(Lock):
        Lock = False
        Tilt = True
    if(Tilt):
        Tilt = False
        Wait = True
    if(Wait):
        Wait = False
        Look = True
