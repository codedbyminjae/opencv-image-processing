import numpy as np
import cv2

# switch case문을 사전(dictionary)으로 구현
switch_case = {
    ord('a'): "a키 입력",                   # ord() 함수- 문자를 아스키코드로 변환
    ord('b'): "b키 입력",
    0x41: "A키 입력",
    int('0x42', 16): "B키 입력",             # 16진수인 0x42를 10진수로 변환하면 66임
    2424832: "왼쪽 화살표키 입력",           # 0x250000
    2490368: "윗쪽 화살표키 입력",           # 0x260000
    2555904: "오른쪽 화살표키 입력",         # 0x270000
    2621440: "아래쪽 화살표키 입력"          # 0x280000
}

image = np.ones((200, 300), np.float64)       # 화소값이 1인 행렬 생성
win_name = 'Keyboard Event'
cv2.namedWindow(win_name)                     # 윈도우 이름
cv2.imshow(win_name, image)

# 윈도우 초기 위치
x, y = 100, 100
cv2.moveWindow(win_name, x, y)

while True:                                   # 무한 반복
    key = cv2.waitKeyEx(100)                  # 100ms 동안 키 이벤트 대기
    if key == 27:  # ESC 키 누르면 종료
        break
    elif key == -1:
        continue
    else:
        if key < 255:
            print(key, chr(key))
        else:
            print(key)

        # 방향키 입력에 따라 창 위치 이동
        if key == 2424832:   # 왼쪽 화살표
            x -= 10
        elif key == 2555904: # 오른쪽 화살표
            x += 10
        elif key == 2490368: # 위쪽 화살표
            y -= 10
        elif key == 2621440: # 아래쪽 화살표
            y += 10

        cv2.moveWindow(win_name, x, y)

cv2.destroyAllWindows()                       # 열린 모든 윈도우 제거
