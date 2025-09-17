import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8) # numpy의 행과 열 <--> openCV의 x, y 위치 좌표 (서로 반대 주의)
image [ : ] = 200

title1, title2 = 'Position1', 'Position2'

# 오토사이즈여서 title1은 사이즈 조정 불가능
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE) # default : cv2.WINDOW_AUTOSIZE
cv2.namedWindow(title2, cv2.WINDOW_NORMAL) # 윈도우 크기 변경 가능, 내부 색상변화도 같이 동시에 가능
cv2.waitKey(0)

cv2.moveWindow(title1, 150, 150)
cv2.moveWindow(title2, 400, 50)
cv2.waitKey(0)

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.waitKey(0)

cv2.resizeWindow(title1, 600, 300)
cv2.resizeWindow(title2, 600, 300)
cv2.waitKey(0)

cv2.destroyAllWindows()