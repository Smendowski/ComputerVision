import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:

	ret, frame = cap.read()
	# Hue - Color
	# Saturation - Intensity
	# Value - Brightness
	# low_green = np.array([hue, saturation, value])
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Red Color Range and Mask 
	low_red = np.array([161, 155, 84])
	high_red = np.array([179, 255, 255])
	mask_red = cv2.inRange(hsv_frame, low_red, high_red)
	# Only allowed color can be seen - represented by white
	# Bitwise and to turn into proper color 
	red_frame = cv2.bitwise_and(frame, frame, mask = mask_red)

	# Blue
	low_blue = np.array([94, 80, 2])
	high_blue = np.array([126, 255, 255])
	mask_blue = cv2.inRange(hsv_frame, low_blue, high_blue)
	blue_frame = cv2.bitwise_and(frame, frame, mask = mask_blue)

	#Green 
	low_green = np.array([25, 52, 72])
	high_green = np.array([102, 255, 255])
	mask_green = cv2.inRange(hsv_frame, low_green, high_green)
	green_frame = cv2.bitwise_and(frame, frame, mask = mask_green)

	# !White
	low = np.array([0, 42, 0])
	hight = np.array([179, 255, 255])
	mask = cv2.inRange(hsv_frame, low, hight)
	no_white_frame = cv2.bitwise_and(frame, frame, mask = mask)


	
	cv2.imshow("Red", red_frame)
	cv2.imshow("Blue", blue_frame)
	cv2.imshow("Green", green_frame)
	cv2.imshow("NoWhite", no_white_frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()