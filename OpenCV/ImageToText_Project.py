import cv2
import numpy as np
import pytesseract

TESSERACT_PATH = "C:/Program Files/Tesseract-OCR/tesseract.exe" #테서렉스 설치 경로
imgpath='OpenCVproject.jpg'  #이미지 파일 경로
win_name = "Image To Text"  #OpenCV 창 이름
img = cv2.imread(imgpath)   #이미지 읽어오기
image = cv2.resize(img, dsize=(0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

xy = []
#마우스 이벤트 처리 함수
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x,y), 3, (0,255,0), 5)
        cv2.imshow(win_name, image)
        xy.append((x,y))

        if len(xy) == 4:
            pts1 = np.array([xy[0], xy[1], xy[2], xy[3]], np.float32)
            pts2 = np.array([(50,60), (450,60), (50,320), (450,320)], np.float32)
            perspect_mat = cv2.getPerspectiveTransform(pts1, pts2)
            dst = cv2.warpPerspective(image, perspect_mat, (480,380),
                                    cv2.INTER_CUBIC)
            cv2.imshow('dst_perspective', dst)
            ImgProcessing(dst)
    return 0


#이미지 처리 함수
def ImgProcessing(dst):
    while True:
        key = cv2.waitKeyEx(100)
        if key == 13: 
            image = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
            cv2.imshow("img_gray", image)
            break
    # image = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("img_gray", image)
    GetOCR(image)
    return 0


#OCR 함수
def GetOCR(image):
    #이미지 불러오기
    while True:
        key = cv2.waitKeyEx(100)
        if key == 13: 
            pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
            text = pytesseract.image_to_string(image, lang='kor+eng')
            print(text)
            break

    #OCR모델 불러오기
    # pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

    # #OCR모델로 글자 추출
    # text = pytesseract.image_to_string(image, lang='kor+eng')
    # print(text)
        
    return text


cv2.imshow(win_name, image)   #이미지 출력
cv2.setMouseCallback(win_name, onMouse)
cv2.waitKey(0)              #입력 대기

# text = GetOCR()             #OCR함수로 텍스트 추출
# print(text)                 #텍스트 출력