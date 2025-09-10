import cv2
import matplotlib.pyplot as plt
import numpy as np

# 이미지 생성 및 OpenCV 테스트
img = np.zeros((300, 300, 3), dtype=np.uint8)
cv2.circle(img, (150, 150), 100, (255, 0, 0), -1)  # 파란 원 그리기

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("OpenCV Test Image")
plt.axis('off')
plt.show()
