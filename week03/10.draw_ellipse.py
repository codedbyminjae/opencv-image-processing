import numpy as np
import cv2

orange, blue, white = (0, 165, 255), (255, 0, 0), (255,255,255) # 색상 지정
image = np.full((300, 700, 3), white, np.uint8)

pt1, pt2 = (180, 150), (550, 150) # 타원 중심점
size = (120, 60) # 타원 크기 - 반지름 값임

cv2.circle(image, pt1, 1, 0, 2) # 타원의 중심점(2화소 원) 표시
cv2.circle(image, pt2, 1, 0, 2)

cv2.ellipse(image, pt1, size,  0, 0, 360, blue, 1) # 0도니까 정상 타원, 0~360 타원 그림 모두 출력
cv2.ellipse(image, pt2, size, 90, 0, 360, blue, 1) # 90도 돌려서
cv2.ellipse(image, pt1, size,  0, 30, 270, orange, 4) # 30도만큼 회전한 축 기준으로 270도 만큼 그리기
cv2.ellipse(image, pt2, size, 90,-45,  90, orange, 4) # 90도 돌린 상태에서 -만큼 45도 가고, 90도 만큼 그리기

cv2.imshow("Draw Eclipse & Arc", image)
cv2.waitKey()                                           # 키입력 대기