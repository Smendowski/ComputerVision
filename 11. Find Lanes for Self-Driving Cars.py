import cv2
import numpy as np
import matplotlib.pyplot as plt

def make_coordinates(image, line_parmeters):
	slope, intercept = line_parmeters
	y1 = image.shape[0]
	y2 = int(y1*(3/5))
	x1 = int((y1 - intercept)/slope)
	x2 = int((y2 - intercept)/slope)
	return np.array([x1, y1, x2, y2])


def average_slope_intercept(image, lines):
	left_fit = []
	right_fit = []
	for line in lines:
		x1,y1,x2,y2 = line.reshape(4)
		parameters = np.polyfit((x1,x2), (y1,y2), 1)
		slope = parameters[0]
		intercept = parameters[1]
		if slope < 0:
			left_fit.append((slope, intercept))
		else:
			right_fit.append((slope, intercept))
	left_fit_average = np.average(left_fit, axis=0)
	right_fit_average = np.average(right_fit, axis=0)
	left_line = make_coordinates(image, left_fit_average)
	right_line = make_coordinates(image, right_fit_average)
	return np.array([left_line, right_line])


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
	masked_image = cv2.bitwise_and(image, mask)
	return masked_image

# To find ROI triangle coordinates
#plt.imshow(lane_canny)
#plt.show()
cropped_image = region_of_interest(lane_canny)

# Hough Transform y = mx + b -> represented by single point (m,b)
# Signle point represented by line function in Hough Space

def display_lines(images, lines):
	line_image = np.zeros_like(image)
	if lines is not None:
		for line in lines:
			x1,y1,x2,y2 = line.reshape(4)
			cv2.line(line_image, (x1,y1), (x2,y2), (255,0,0), 10)
	return line_image


lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100,
	np.array([]), minLineLength=40, maxLineGap=5)

avaraged_lines = avarage_slope_intercept(lane_image, lines)

line_image = display_lines(lane_image, lines)
combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)

cv2.imshow("result", combo_image)
cv2.waitKey(0)
