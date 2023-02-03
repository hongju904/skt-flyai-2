import numpy as np, cv2

image = cv2.imread("ch08_images/translate.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("에러")

M = np.array([ [1,0,100],
                [0,1,100]], dtype=np.float32)
dst = cv2.warpAffine(image, M, (0,0))

cv2.imshow('image', image)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()