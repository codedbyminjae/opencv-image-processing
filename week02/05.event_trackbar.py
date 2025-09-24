import numpy as np
import cv2

def onChange(value): # 트랙바 콜백 함수
    global image # 전역 변수 참조

    # int로 형변환 해주는게 맞다
    add_value = value - int(image[0][0]) # 트랙바 값과 영상 화소값 차분
    print("추가 화소값:", add_value)
    if  add_value > 0 : image = image + add_value # 행렬과 스칼라 덧셈 수행
    else: image = image - abs(add_value) # 행렬과 스칼라 덧셈 수행
    cv2.imshow(title, image)

image = np.zeros((300, 500), np.uint8) # 영상 생성

title = 'Trackbar Event'
cv2.imshow(title, image)
# 음수값이 unsigned 로 가게 되면 큰 양수값으로 가기 때문에 205로 출력
cv2.createTrackbar("Brightness", title, image[0][0], 255, onChange)	# 트랙바 콜백 함수 등록
cv2.waitKey(0)
cv2.destroyWindow()