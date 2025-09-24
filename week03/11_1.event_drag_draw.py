import numpy as np
import cv2

# 초기 설정
drawing = False          # 마우스 드래그 상태 여부
mode = 'rect'            # 'rect' 또는 'circle' 선택 가능
start_pt = (-1, -1)      # 드래그 시작점
title = "Draw by Drag"

# 흰색 배경 이미지
image = np.full((300, 500, 3), 255, np.uint8)
temp_img = image.copy()  # 미리보기용 임시 이미지

def onMouse(event, x, y, flags, param):
    global start_pt, drawing, image, temp_img, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_pt = (x, y)
        temp_img = image.copy()  # 새로 시작할 때 원본 복사

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp_img = image.copy()  # 도형을 그릴 때마다 새로 그리기
            if mode == 'rect':
                cv2.rectangle(temp_img, start_pt, (x, y), (255, 0, 0), 2)
            elif mode == 'circle':
                dx, dy = x - start_pt[0], y - start_pt[1]
                radius = int(np.sqrt(dx**2 + dy**2))
                cv2.circle(temp_img, start_pt, radius, (0, 0, 255), 2)
            cv2.imshow(title, temp_img)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == 'rect':
            cv2.rectangle(image, start_pt, (x, y), (255, 0, 0), 2)
        elif mode == 'circle':
            dx, dy = x - start_pt[0], y - start_pt[1]
            radius = int(np.sqrt(dx**2 + dy**2))
            cv2.circle(image, start_pt, radius, (0, 0, 255), 2)
        cv2.imshow(title, image)

cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
