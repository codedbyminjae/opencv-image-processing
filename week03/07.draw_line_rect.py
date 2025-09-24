import numpy as np
import cv2

# color: 선 색상 RGB가 아니라 BGR <- openCV는 일반 RGB와 순서가 다르다.

blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
image = np.zeros((400, 600, 3), np.uint8) # np는 행 열 = 높이가 행, 폭이 열
image [ : ] = (255, 255, 255) # 흰색 배경
#image = np.full ((400,600,3), (255,255,255), np.uint8)

pt1, pt2 = (50, 50), (250, 150) # (x,y) 좌표계, lib에 따라 다르다.
pt3, pt4 = (400, 150), (500, 50)
roi = (50, 200, 200, 100) # 옆으로 긴 사각형

# 직선 그리기
cv2.line(image, pt1, pt2, red)
cv2.line(image, pt3, pt4, green, 3, cv2.LINE_AA)
cv2.imshow('Line & Rectangle', image)
cv2.waitKey(0)

# 사각형 그리기
cv2.rectangle(image, pt1, pt2, blue, 3, cv2.LINE_4)
cv2.rectangle(image, roi, red, 3, cv2.LINE_8)
cv2.rectangle(image, (400, 200, 100, 100), green, cv2.FILLED) #시작 위치와 위드 헤이트

cv2.imshow('Line & Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
