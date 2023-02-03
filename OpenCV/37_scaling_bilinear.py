import numpy as np, cv2

image = cv2.imread('ch08_images/interpolation.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("에러")

size = (350, 400)
dst3 = cv2.resize(image, size, cv2.INTER_LINEAR)
dst4 = cv2.resize(image, size, cv2.INTER_NEAREST)

cv2.imshow("image", image)
cv2.imshow("OpenCV_bilinear", dst3)
cv2.imshow("OenCV_Nearest", dst4)
cv2.waitKey(0)