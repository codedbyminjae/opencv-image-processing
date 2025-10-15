import numpy as np, cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/gray_gradient256.jpg', cv2.IMREAD_GRAYSCALE)

thresh_np = np.zeros_like(img) # 검은색 이미지
thresh_np[img>127] = 255 # 127 보다 큰 값만 255(흰색)으로 변경

ret, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

imgs = {'Original':img, 'Numpy API':thresh_np, 'cv2.threshold':thresh_cv}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks((0, 127, 255)); plt.yticks([])

plt.show()