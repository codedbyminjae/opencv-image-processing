import numpy as np
import cv2

# 이벤트, 포인터 위치 (x, y), 플래그 여부, 추가 파라미터 선언
def onMouse(event, x, y, flags, param):
    global title, pt, drawing, shape_mode # 전역 변수 선언, 초기 좌표와 드래그 여부 판단 변수 추가

    # 마우스 좌클릭 클릭 이벤트
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        pt = (x, y)
        shape_mode = 'rect'

    # 마우스 우클릭 클릭 이벤트
    elif event == cv2.EVENT_RBUTTONDOWN:
        drawing = True
        pt = (x, y)
        shape_mode = 'circle'

    # 마우스 움직이는 중 drawing -> True 일때 도형이 보여지는 함수
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if shape_mode == 'rect':
                cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)
            elif shape_mode == 'circle':
                dx = x - pt[0]
                dy = y - pt[1]
                radius = int(np.sqrt(dx ** 2 + dy ** 2))
                cv2.circle(image, pt, radius, (0, 0, 255), 2)
            cv2.imshow(title, image)
        elif drawing == False:
            pass

    # 마우스 좌클릭 클릭 해제 이벤트
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_pt = (x, y)
        cv2.rectangle(image, pt, end_pt, (255, 0, 0), 2)
        cv2.imshow(title, image)

    # 마우스 우클릭 클릭 해제 이벤트
    elif event == cv2.EVENT_RBUTTONUP:
        drawing = False
        dx = x - pt[0]
        dy = y - pt[1]
        radius = int(np.sqrt(dx ** 2 + dy ** 2))
        cv2.circle(image, pt, radius, (0, 0, 255), 3)
        cv2.imshow(title, image)

image = np.full((300, 500, 3), (255, 255, 255), np.uint8)
pt = (-1, -1)
drawing = False
shape_mode = None
title = "Draw Event Practice - Drag & Rubber Band"

cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
