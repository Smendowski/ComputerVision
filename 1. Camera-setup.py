import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Changing Resolution 
def make_1080p():
	cap.set(3,1920)
	cap.set(4,1080)

def make_720():
	cap.set(3, 1280)
	cap.set(4, 720)

def make_480():
	cap.set(3, 640)
	cap.set(4, 480)

# Customize Resolution
def custom_resolution(width, height):
	cap.set(3, width)
	cap.set(4, height)	

# Rescaling Frame  percent/100 times
def rescale_frame(frame, percent=75):
	scale_in_percents = percent;
	width = int(frame.shape[1] * scale_in_percents / 100)
	height = int(frame.shape[0] * scale_in_percents / 100)
	dimensions = (width, height)
	return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)



while True:
	 # Capture frame-by-frame
    ret, frame = cap.read()
    frame = rescale_frame(frame, percent=50)
    # Operation on frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame2 = rescale_frame(frame, percent=70 )
    cv2.imshow('frame',gray)
    cv2.imshow('frame1', frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
