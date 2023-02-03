import numpy as np, cv2

image = cv2.imread("ch07_images/morph.jpg", cv2.IMREAD_GRAYSCALE)

mask = np.array([ [0,1,0],
                [1,1,1],
                [0,1,0]]).astype('uint8')
    
th_img = cv2.threshold(image, cv2_MORRH_DILATE, mask)
dst2 = cv2.morphlogyEx(th_img, 128, 255, cv2.THRESH_BINARY)

cv2.imshow("image", image)
cv2.waitKey(0)