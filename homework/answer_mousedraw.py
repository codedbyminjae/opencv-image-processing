import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global title, pt, drag, pre

    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN:
        pt = pre = (x, y)
        drag = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drag:
            if flags & (cv2.EVENT_FLAG_LBUTTON | cv2.EVENT_FLAG_RBUTTON):
                cv2.line(image, pt, pre, (255,255,255), 1)
                cv2.line(image, pt, (x, y), (0, 255, 0), 1)
                pre = (x, y)
                cv2.imshow(title, image)

    elif event == cv2.EVENT_LBUTTONUP:
        drag = False
        if pt == (x, y):
            return
        else:
            cv2.line(image, pt, pre, (255,255,255), 1)
            cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)
            cv2.imshow(title, image)

    elif event == cv2.EVENT_RBUTTONUP:
        drag = False
        if pt == (x, y):
            return
        else:
            dx, dy = pt[0] - x, pt[1] - y
            radius = int(np.sqrt(dx**2 + dy**2))
            cv2.line(image, pt, pre, (255,255,255), 1)
            cv2.circle(image, pt, radius, (0, 0, 255), 2)
            cv2.imshow(title, image)


image = np.full((300, 500, 3), 255, np.uint8)

pt = (-1, -1)
pre = (-1, -1)
drag = False
title = "Draw Event Practice - Drag & Rubber Band"

cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
