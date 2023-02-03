import numpy as np, math, cv2

image = cv2.imread('ch08_images/perspective.jpg', cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")

pts1 = np.array([(80,40), (315,133), (75,300), (335,300)], np.float32)
pts2 = np.array([(50,60), (340,60), (50,320), (340,320)], np.float32)

perspect_mat = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(image, perspect_mat, image.shape[1::-1],
                            cv2.INTER_CUBIC)

print("[perspect_mat] = \n%s\n" % perspect_mat)

cv2.imshow('image', image)
cv2.imshow('dst_perspective', dst)
cv2.waitKey(0)