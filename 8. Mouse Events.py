import cv2
import numpy as np


# Listing Mouse and Keyboard events
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# Callable functions
def coordinates_and_rgb_events(event, x_pointed, y_pointed, flags, param):
	font_family = cv2.FONT_HERSHEY_SIMPLEX
	font_bold = 2
	font_size = 0.8

	if event == cv2.EVENT_LBUTTONDOWN:
		font_color1 = (255,255,255)
		coordinatesInfo = str(x_pointed) + ', ' + str(y_pointed)
		cv2.putText(BG, coordinatesInfo, (x_pointed, y_pointed), 
			font_family, font_size, font_color1, font_bold)
		cv2.imshow('background', BG)

	if event == cv2.EVENT_RBUTTONDOWN:
		font_color2 = (255,255,0)
		blue_channel_idx = 0
		green_channel_idx = 1
		red_channel_idx = 2
		blue = BG[y_pointed, x_pointed, blue_channel_idx]
		green = BG[y_pointed, x_pointed, green_channel_idx]
		red = BG[y_pointed, x_pointed, red_channel_idx]
		colorsInfo = str(blue) + ', ' + str(green) + ', ' + str(red)
		cv2.putText(BG, colorsInfo, (x_pointed, y_pointed), font_family,
			font_size, font_color2, font_bold)
		cv2.imshow('background', BG)

def connect_points_event(event, x_pointed, y_pointed, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		radius = 3 # Imitation of dot
		thickness = -1 # Circle is filled with a color
		cv2.circle(BG, (x_pointed, y_pointed), radius, (0,0,255), thickness)
		points.append((x_pointed, y_pointed))
		if len(points) >= 2:
			cv2.line(BG, points[-1], points[-2], (189,43,14), 5)
		cv2.imshow('background', BG)



BG = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('background', BG)
points = []

#cv2.setMouseCallback('background', coordinates_and_rgb_events)
cv2.setMouseCallback('background', connect_points_event)

cv2.waitKey(0)
cv2.destroyAllWindows()




