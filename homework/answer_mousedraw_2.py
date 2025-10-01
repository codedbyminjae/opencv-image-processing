import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global pt, drag, image, temp, title

    # 마우스 버튼 누름
    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN:
        pt = (x, y)
        drag = True

    # 마우스 이동 (드래그 중일 때)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drag:
            temp = image.copy()  # 원본을 복사해서 미리보기 화면 생성
            if flags & cv2.EVENT_FLAG_LBUTTON:   # 좌클릭 → 사각형 미리보기
                cv2.rectangle(temp, pt, (x, y), (255, 0, 0), 2)
            elif flags & cv2.EVENT_FLAG_RBUTTON: # 우클릭 → 원 미리보기
                dx, dy = pt[0] - x, pt[1] - y
                radius = int(np.sqrt(dx**2 + dy**2))
                cv2.circle(temp, pt, radius, (0, 0, 255), 2)
            cv2.imshow(title, temp)

    # 왼쪽 버튼 뗄 때 → 사각형 확정
    elif event == cv2.EVENT_LBUTTONUP:
        drag = False
        if pt != (x, y):
            cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)
            cv2.imshow(title, image)

    # 오른쪽 버튼 뗄 때 → 원 확정
    elif event == cv2.EVENT_RBUTTONUP:
        drag = False
        if pt != (x, y):
            dx, dy = pt[0] - x, pt[1] - y
            radius = int(np.sqrt(dx**2 + dy**2))
            cv2.circle(image, pt, radius, (0, 0, 255), 2)
            cv2.imshow(title, image)


# ====== 초기 설정 ======
image = np.full((300, 500, 3), 255, np.uint8)
temp = image.copy()

pt = (-1, -1)
drag = False
title = "Draw Event Practice - Drag & Rubber Band"

cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
