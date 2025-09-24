import numpy as np
import cv2

def onChange(value):
    global image, title
    add_value = value - image[0][0]
    image = np.clip(image + add_value, 0, 255)
    cv2.imshow(title, image)

def onMouse(event, x, y, flags, param):
    global image, bar_name, title
    if event == cv2.EVENT_RBUTTONDOWN:  # 오른쪽 클릭 → 밝기 증가
        if image[0][0] < 246:
            image += 10
            cv2.setTrackbarPos(bar_name, title, int(image[0][0]))
            cv2.imshow(title, image)
    elif event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 클릭 → 밝기 감소
        if image[0][0] >= 10:
            image -= 10
            cv2.setTrackbarPos(bar_name, title, int(image[0][0]))
            cv2.imshow(title, image)

# 초기 세팅
image = np.zeros((300, 500), np.uint8)
title = "Brightness Control"
bar_name = "Brightness"

cv2.imshow(title, image)
cv2.createTrackbar(bar_name, title, int(image[0][0]), 255, onChange)
cv2.setMouseCallback(title, onMouse)

while True:
    key = cv2.waitKey(0)

    if key == 27:  # ESC 종료
        break
    elif key == ord('a'):  # a 키 → 밝기 감소
        if image[0][0] >= 10:
            image -= 10
            cv2.setTrackbarPos(bar_name, title, int(image[0][0]))
            cv2.imshow(title, image)
    elif key == ord('d'):  # d 키 → 밝기 증가
        if image[0][0] < 246:
            image += 10
            cv2.setTrackbarPos(bar_name, title, int(image[0][0]))
            cv2.imshow(title, image)
cv2.destroyAllWindows()
