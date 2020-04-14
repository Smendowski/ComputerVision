import numpy as np
import cv2
import os
import time
import datetime
import glob
from utilities import VideoConfig, image_resize

cap = cv2.VideoCapture(0)
save_path = 'timelapse.mp4'
img_dir = "images/timelapse/"

if not os.path.exists(timelapse_dir):
	os.mkdir(timelapse_dir)

frames_per_seconds = 24.0
config = VideoConfig(cap, filepath=save_path, res='720')
out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)


now = datetime.datetime.now()
end = now + datetime.timedelta(seconds=20)

iteration_value = 0 

while datetime.datetime.now() < end:

	ret, frame = cap.read()
	filename = f"{img_dir}/{iteration_value}.jpg"
	iteration_value += 1
	cv2.imwrite(filename, frame)

	time.sleep(seconds=2)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break


clear_images = True

def images_to_video(out, img_dir, clear_images=True)
	image_list = glob.glob(f"{img_dir}/*.jpg")
	sorted_images = sorted(image_list, key=os.path.getmtime)

	for file in sorted_images:
		image_frame = cv2.imread(file)
		out.write(image_frame)

	if clear_images:
		for file in image_list:
			os.remove(file)


images_to_video(out, img_dir, clear_images=True)

cap.release()
out.release()
cv2.destroyAllWindows()