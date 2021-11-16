# This script will detect faces via your webcam.
# Tested with OpenCV3

# import opencv
import cv2

# import servokit to have pi move servos
from adafruit_servokit import ServoKit
# there are 16 channels on the servo kit
kit = ServoKit(channels=16)
# capture "video" from default camera
cap = cv2.VideoCapture(0)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# sets the fps of the video capturing to 15
cap.set(cv2.CAP_PROP_FPS , 15)
# what is the width of the frame we are capturing
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

#loop
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# grayscale the captured frame
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	print("Found {0} faces!".format(len(faces)))
	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		print("x + w / 2: " + str((2*x+w)/2))
		print("width + " + str(width))
		if (2*x + w)/2 > (width/2+25):
			kit.servo[0].angle = (100)
		elif (2*x + w)/2 < (width/2-25):
			kit.servo[0].angle = (80)
		else:
			kit.servo[0].angle = (90)


	# Display the resulting frame
	# cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
