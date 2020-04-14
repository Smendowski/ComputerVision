import numpy as np
import cv2
from utilities import image_resize

w_icon = cv2.imread('images/watermark/icon.png', -1)
watermark = image_resize(w_icon, height=50)
watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2BGRA)
#cv2.imshow('watermark', watermark)

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	# Adjusting frame Colors type to be the same as Overlay
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
	
	color = (255,0,0) 
	bold = 2
	start_cord_x = 50
	start_cord_y = 150
	rectangle_width = 100
	rectangle_height = 200
	end_cord_x = start_cord_x + rectangle_width
	end_cord_y = start_cord_y + rectangle_height
	cv2.rectangle(frame, (start_cord_x,start_cord_y), (end_cord_x, end_cord_y),
		 color, bold)


	frame_height, frame_width, frame_channels = frame.shape
	# if frame in grayscale, frame.shape do not returns frame_channels

	# Overlay - 4 channels BGR and Aplha
	overlay = np.zeros((frame_height, frame_width, 4), dtype='uint8')
	overlay[100:250, 100:125] = (255,0,0,1) # B,G,R,Alpha
	
	watermark_height, watermark_width, watermark_channels =  watermark.shape
	for i in range(0, watermark_height):
		for j in range(0, watermark_width):
			if watermark[i,j][3] != 0:	
				height_offset = frame_height - watermark_height - 10
				width_offset = frame_width - watermark_width - 10
				overlay[height_offset + i, width_offset + j] = watermark[i,j] 

	# Adding overlay - new on frame
	cv2.addWeighted(overlay, 0.25, frame, 1.0, 0, frame)

	#print(frame[start_cord_x:end_cord_x, start_cord_y:end_cord_y])
	cv2.imshow('frame', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break


cap.release()
out.release()
cv2.destroyAllWindows()		


# To add watermark I've created an overlay with exactly
# same size as frame, and replaced it's part with a
# watermark icon. 

