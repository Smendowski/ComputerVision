import numpy as np
import cv2

# 252x252, 3 channels, - zeros => full black background
img1 = np.zeros((252,252,3), np.uint8)
# placing rectanlge (200(y) x 200(x)),  -1 -> fill with color
img1 = cv2.rectangle(img1, (200,200), (50,50), (255,255,255), -1)
img2 = cv2.imread("images/BlackWhite.jpg")

# White represents logical 1, black logical 0

bitwiseAnd = cv2.bitwise_and(img1, img2)
bitwiseOr = cv2.bitwise_or(img1, img2)
bitwiseXOr = cv2.bitwise_xor(img1, img2)
bitwiseNotImg1 = cv2.bitwise_not(img1)
bitwiseNotImg2 = cv2.bitwise_not(img2)


cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("Bitwise And", bitwiseAnd)
cv2.imshow("Bitwise Or", bitwiseOr)
cv2.imshow("Bitwise XOr", bitwiseXOr)
cv2.imshow("Img1 Bitwise Not", bitwiseNotImg1)
cv2.imshow("Img2 Bitwise Not", bitwiseNotImg2)

cv2.waitKey(0)
cv2.destroyAllWindows()