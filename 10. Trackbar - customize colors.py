import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('Window')

def print_value(trackbar_position):
	print(trackbar_position)

# Tracbar Start (0) and Stop (255) Values
cv2.createTrackbar('B', 'Window', 0, 255, print_value)
cv2.createTrackbar('G', 'Window', 0, 255, print_value)
cv2.createTrackbar('R', 'Window', 0, 255, print_value)

while True:
	cv2.imshow('Window', img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	blue = cv2.getTrackbarPos('B', 'Window')
	green = cv2.getTrackbarPos('G', 'Window')
	red = cv2.getTrackbarPos('R', 'Window')

	img[:] = [blue, green, red]	    


cv2.destroyAllWindows()