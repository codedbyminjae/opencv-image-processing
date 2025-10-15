import numpy as np, cv2

img = np.zeros((100,256), dtype=np.uint8)
for i in range(100):
    for j in range(256):
        img[i,j] = j
cv2.imshow('img', img)
cv2.imwrite('images/gray_gradient256.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()