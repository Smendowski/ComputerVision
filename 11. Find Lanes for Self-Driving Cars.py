import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("images/Self-DrivingCars/CarLanes1.png")
# 1st step - Convert image to grayscale
# GrayScale image = 1 channel processing is faster than 3 channels BGR
lane_image = np.copy(image)
lane_gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

# 2nd step - Reduce Noise using Gausian Blur
lane_blurred = cv2.GaussianBlur(lane_gray, (5,5), 0)

# 3rd step - Apply Canny() to detect edges, detect the strongest gradient
# edges coresponds to the most rapid changes in brightness
low_threshold = 50
high_threshold = 150
lane_canny = cv2.Canny(lane_blurred, low_threshold, high_threshold)

# 4th step - Finding Lane Lines - Defining Region of Interest
def region_of_interest(image):
	height = image.shape[0]
	polygons = np.array([
		[(0, height), (1100, height), (650, 250)]
		])
	mask = np.zeros_like(image)
	# polygons needs to be an np Array
	cv2.fillPoly(mask, polygons, 255)
	return mask

# To find ROI triangle coordinates
#plt.imshow(lane_canny)
#plt.show()

cv2.imshow("result", region_of_interest(lane_canny))
cv2.waitKey(0)
