import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global title, pt

    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            cv2.rectangle(image, pt, (x, y),  (255, 0, 0), 2)
            cv2.imshow(title, image)
            pt = (-1, -1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            # 주석 내용은 원을 직사각형처럼 처리하려면 하기 위한 코드
            # dx, dy = (pt[0]-x)/2, (pt[1] - y)/2
            dx, dy = pt[0] - x, pt[1] - y
            radius = (int(np.sqrt(dx**2 + dy**2)))
            center = int(pt[0] - dx), int(pt[1] - dy)
            # cv2.circle(image, center, radius, (0,0,255), 2)
            cv2.circle (image, pt, radius, (0, 0, 255), 3)
            cv2.imshow(title, image)
            pt = (-1, -1)

image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

pt = (-1, -1)
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()