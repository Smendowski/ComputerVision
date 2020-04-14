import numpy as np
import cv2
import math
import glob
from utilities import VideoConfig, image_resize

cap = cv2.VideoCapture(0)

frames_per_second = 24.0
save_path = 'filter.mp4'
config = VideoConfig(cap, filepath=save_path, res='480')


def apply_invert(frame):
	return cv2.bitwise_not(frame)

def apply_color_overlay(frame, intensity=0.5, blue=20, green=66, red=112):
	frame = check_alpha_channel(frame)
	frame_height, frame_width, frame_channels = frame.shape 
	color_bgra = (blue, green, red, 1)
	overlay = np.full((frame_height, frame_width, 4), color_bgra, dtype='uint8')
	cv2.addWeighted(overlay, intensity, frame, 1.0, 0, frame)
	# Turn back to 3 channels
	frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
	return frame

def apply_sepia(frame, intensity=0.5):
	blue = 20
	green = 66
	red = 112
	frame = apply_color_overlay(frame, intensity=intensity, blue=blue, green=green, red=red)
	return frame


def alpha_blend(frame_1, frame_2, mask):
    alpha = mask/255.0 
    blended = cv2.convertScaleAbs(frame_1*(1-alpha) + frame_2*alpha)
    return blended


def apply_circle_focus_blur(frame, intensity=0.2):
    frame = check_alpha_channel(frame)
    frame_h, frame_w, frame_c = frame.shape
    y = int(frame_h/2)
    x = int(frame_w/2)

    mask = np.zeros((frame_h, frame_w, 4), dtype='uint8')
    cv2.circle(mask, (x, y), int(y/2), (255,255,255), -1, cv2.LINE_AA)
    mask = cv2.GaussianBlur(mask, (21,21),11 )

    blured = cv2.GaussianBlur(frame, (21,21), 11)
    blended = alpha_blend(frame, blured, 255-mask)
    frame = cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)
    return frame

def check_alpha_channel(frame):
	try:
		frame.shape[3]
	except IndexError:
		# Applying 4th Aplha channel
		# 3 channels B,G,R and 4th Alpha - like opacity in CSS, rgba
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
	return frame


while True:
	ret, frame = cap.read()
	invert = apply_invert(frame.copy())
	sepia = apply_sepia(frame.copy())
	blured = apply_circle_focus_blur(frame.copy())

	cv2.imshow('frame', frame)
	cv2.imshow('sepia', sepia)
	cv2.imshow('invert', invert)
	cv2.imshow('blur', blur)

	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.releas()
cv2.destroyAllWindows