import numpy as np
import cv2
import os

VIEDO_DIMENSIONS = {
	"480p" : (640, 480),
	"720p" : (1280, 720),
	"1080p": (1920, 1080),
	"4k" : (3840, 2160),
}

def change_resolution(cap, width, height):
	cap.set(3, width)
	cap.set(4, height)

def get_dimension(cap, res='1080p'):
	# Standard Option in case of bad res passed
	width, height = VIEDO_DIMENSIONS['480p']
	if res in VIEDO_DIMENSIONS:
		width,height = VIEDO_DIMENSIONS[res]
	change_resolution(cap, width, height)
	return width, height	


filename = 'video.avi' # .mp4 also works
frames_per_second = 24.0
my_resolution = '720p'


VIDEO_TYPE ={
	'avi' : cv2.VideoWriter_fourcc(*'XVID'),
	'mp4' : cv2.VideoWriter_fourcc(*'XVID')
	# fourcc - video codecs sources
}

def get_video_type(filename):
	# filename.ext
	filename, ext = os.path.splitext(filename)
	if ext in VIDEO_TYPE:
		return VIDEO_TYPE[ext]
	return	VIDEO_TYPE['avi']




cap = cv2.VideoCapture(0)
dimensions = get_dimension(cap, res=my_resolution)
my_video_type = get_video_type(filename)

out = cv2.VideoWriter(filename, my_video_type, frames_per_second,
	dimensions)
# instead of dimenstions, we can ass width and height

while True:
	ret, frame = cap.read()
	out.write(frame)
	cv2.imshow('frame', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()		